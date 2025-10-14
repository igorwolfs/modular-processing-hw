# Possible Choices

## STM32H72

- PRO: 
	- better ecosystem
	- Non-BGA
	- Easier development
	- DSP capabiltiy
	- SRAM/SDRAM/PSRAM (max frequency: 150 MHz)
- CON: 
	- more expensive
	- No RGMII
	- External RAM required

## Allwinner

- PRO:
	- Non-BGA
	- Cheaper
	- RGMII
- CON:
	- parallel inputs channel?
	- Support?

It seems in general that Allwinner is not used that often in devices.


# CPU requirements
The most important requirements for the CPU are
- There must be an ethernet interface (preferably RGMII, RMII also allowed)
- There must be a ULPI interface for HI-SPEED USB2.0
- There must be an SDRAM / SRAM / PSRAM  controller
- The clock speed must be above 200 MHz, the data to be read from the ADC (MS)
	- This one has a 10-bit pin interface.
- The package MUST NOT be a BGA, these are way too hard to debug.
- 1 MCO output to drive the ADC

## ADC
### Internal ADC
- Single / dual channel ADC
- 

### Alternative
- Downsampling / decimation of ADC data before in small DSP CPU

## USB
- ULPI interface

## SDRAM
### Data transfer requirements
- Data transfer:
	- 30 MHz x 2 bytes -> 57.3 Mbytes / second
	- Should be able to save at least a second of data

### Peripheral (stm32h72)
FMC (Flexible memory controller), can handle
- SRAM
- NOR flash / OneNAND flash
- PSRAM
- NAND
- DRAM (SDRAM Mobile LPSDR SDRAM)


#### Busses
- Address bus
	- Single address bus for all peripherals
- Different chip select for all peripherals
- Data bus
	- 8, 16 or 32-bits wide

#### Specs (SDRAM)
- SDRAM: Maximum speed for synchronous access is:
	- The FMC_CLK / FMC_SDCLK frequency divided by 2
- Address bit 13 max
- 2 NSS bits
- Write / Read fifos (16x32 bits)

Check the devboard for comparison
- SDRAM conflicts with

#### Banks
Bank 1 (NOR / PSRAM)
- Chip Selects: can handle 4x64 MB = 256 MB

Bank 2, 4
- Not used

Bank 3:
- Addressing NAND flash memory devices

Bank 5, 6:
- SDRAM devices: each bank here can handle 4 x 64 = 256 MB -> 512 MB togethery
- NOTE: SDRAM and ULPI interface are mutually exclusive!

## Ethernet
- RGMII interface

## DSP
- Full DSP instruction set

### FMAC
- Fixed point multiplier and accumulator
	- 16x16 bit multiplication
	- Can realize FIR and IIR filters

## SPI
### Specs
- SPI, QSPI, OCTSPI all possible 
	- OCTSPI mostly used for hyperbus (memory)
- Max SPI speed


## Clock output
- 2 x MCO output

Note: Input clock for MS9280 is +5 / +3V3 CMOS

## Parallel interfaces
Note: 
- The input data comes from the MS9280 A/D converter at 35 MHz. CMOS 3V3 or CMOS 5V (depending on input voltage)
	- LOW: 0.4 V
	- High: 2.8 V

### Camera interface
- 8-14 bit camera interface
- DCMII: CMOS 8-14 bit parallel interface, with data-rates up to 140 Mbyte/s at a 80 MHz clock

### 16-bit parallel slave synchronous interface
- CMOS / Parallel LVDS style serializer
	- PSSI: synchronou 8/16-bit data in/out slave
		- contains 8-word fifo
		- Can reach up to 140 MByte/s, 80 MHz pixel clock
		- So time multiplexing is A POSSIBILITY!
Choose this one.

### GPIO sampling + DMA
- timer with automatic input sampling and passing on to DMA

## DMA
### DMA2D
- 

# CPU Peripheral Selection
## FMC
FMC 2xSDRAM bus since SDRAM is faster and cheaper. It's the only one providing adequate speed.

### Signals
- Address bus (13 bits): A0..A12
- SDNWE (WE)
- CKE1, CKE2: 2 separate clock enable signals, one for each SDRAM
- NE1, NE2: (NOT) chip enable, one for each SDRAM
- BL0, BL1: Upper and lower byte enable for IC.
- NCAS: CAS# (column select for address)
- NRAS: RAS# (row select for address)


## Parallel Bus
### PSSI 
WARNING: mutually exclusive with the DCMI.

Parallel synchronous slave
- 8 / 16-bit communication between MCU's / MCU and FPGA.
	- Choose 16-bit communication

- Has DMA with 8-word FIFO.
- Data transfer polarity
	- CKPOL = 0:
		- Input sampled on CLOCK FALLING EDGE
		- Output driven on CLOCK RISING EDGE
	- CKPOL = 1:
		- Input sampled on CLOCK RISING EDGE
		- Output driven on CLOCK FALLING EDGE
	- Note: Setting PSSI into sending OR receiving mode can only be done when peripheral is deactivated



### Interrupt
- PSSI_OVR


### Speed
- AHB clock must be >=  2.5 times the frequency
- CLK MAX: 550 MHz
	- 550 / 2.5 = 220 MHz is the absolute maximum

### Pinout
- PSSI_RDY: (output) signal coming from the CPU itself indicating cpu readiness to sample data
- PSSI_VALID: (input) signal coming from another CPU / FPGA indicating data is valid
- PSSI_CLOCK:
	- Clock polarity (data can be captured / transmitted on EITHER rising OR falling edge)
- PSSI_DE: indicates data in the next cycle will be valid and will thus need to be sampled.


## USB
- Battery charger detection
- 12 Mbi/s (full-speed USB)


### Pinout
- USB_OTG_HS_DP
	- Internal 1k5 ohm on D+ line
- USB_OTG_HS_DM
- (USB_OTG_HS_ID) - UNNECESSARY, ONLY FOR USB micro A/B OTG
	- Determines whether device acts as host or peripheral
	- Only possible with USB micro A, micro B
- USB_OTG_HS_VBUS
	- VBUS (5 V) can be connected here
	- CPU has internal regulator capable of regulating its own 3v3 supply
	- Should be connected with a resistive divider of 5_INPUT - 4.7k - VBUS - 10k - GND
- (USB_OTG_HS_SOF) - UNNECESSARY, MOSTLY FOR AUDIO APPLICATIONS


### Question: Does the USB_OTG_HS_VBUS have any use as a Vsense pin when power is supplied externally?
- 


## SPI / SD-CARD
- Add an SPI peripiheral so I can read / write from an sd-card.
	- Might come in handy when saving large amounts of data is necessary (e.g.: when doing testing)

## ADC

### Pinout
- SDMMC2_D0, SDMMC2_D1, SDMMC2_D2, SDMMC2_D3 (Data lines)
- SDMMC_CKN
- SDMMC2_CMD
- SDMMC2_CK

# Power Pin routing / Decoupling
- Check Table 2 in AN5419

## VDD
- 100 nF for each VDD
- 4.7 uF connected to one VDD

## VDDA
- 1 uF ceramic
- 100 nF close to the pin

## VBAT
- Connect to VDD
- 1 uF ceramic
- 100 nF close

## VCAP
- 100 nF close to each VCAP pin
- VCAP pins connected together

## VDD33USB
- 1 uF ceramic
- 100 nF ceramic (if USB reg not used)
- Internally tied to VDD

## VREF+
- 1 uF ceramic
- 100 nF ceramic
- Should be tied to the external reference voltage used for ADC
	- Check voltage used in ADC-board, perhaps provide this voltage to VREF if needed

## PDR_ON
- if HIGH: POR and PDR circuitry is ON
- if LOW: POR and PDR circuitry is OFF
	- So tigh high with 0 ohm resistor