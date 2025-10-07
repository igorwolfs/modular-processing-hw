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


## ADC connections
- 30 MHz MCO output
- CMOS / Parallel LVDS style serializer
	- DCMII: CMOS 8-14 bit parallel interface, with data-rates up to 140 Mbyte/s at a 80 MHz clock
	- PSSI: synchronou 8/16-bit data in/out slave
		- contains 8-word fifo

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

It has a 
- Write fifo
- Read fifo

Maximum speed is
- The FMC_CLK / FMC_SDCLK frequency divided by 2

Check the devboard for comparison.
- SDRAM conflicts with 

## Ethernet
- RGMII interface

## DSP
- Full DSP instruction set
