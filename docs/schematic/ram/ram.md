# CPU Memory Controller
## NOR Flash / PSRAM controller
- Asynchronous SRAM and ROM
- PSRAM (cellurar RAM)
- NOR Flash memory

## Clock speed
- Programmable continuous clock (FMC_CLK) output
	- Can be used as MCO for synchronous access (Read / Write)
- Maximum FMC clock is 150 MHz


# Types of RAM
## PSRAM
- Pseudo-static random access memory
	- Acts as DRAM, looks like SRAM
	- It has internal circuitry for memory refreshing

##  SRAM
Static random access memory. 
- Static: data retainment without refreshing

## DRAM
Dynamic random access memory
- Dynamic: needs refreshing
- Slower than SRAM

# Options

## PSRAM

It seems like PSRAM is a good option, apart from the fact that the biggest size in which I can find it is 64 MBit.

### IS66WVE4M16EBLL-70BLI
64 MBit PSRAM (8 MBytes)
- BGA package (TFBGA-48)
- 4.33 dollars

## SRAM
- Only one availabla seems one with QSPI, and SSOP package
- Seems like I can only find them in small sizes (at most 144 MBit), and at high sizes they are crazy expensive.


### VTI7064MSME
- Too slow (probably QSPI only)
- Good package
- Cheap
- 64 MBit (not enough)

### CY7C2665KV18
- 30 dollars
- 550 MHz clock support

### S27KL0642DPBHI020
- Self refreshing DRAM (PSRAM)
- BGA24
- Hyperbus
- 5.49 dollars


## SDRAM
- They seem to all be in TSOP package, none of them in BGA

### Winbond: W9825G6KH-6
Speed: up to 200 MBit/second

- TSOP-54-10.2mm (non BGA!!!)
- 166 MHz
- 256 Mbit (32 MByte)
- 1.38 dollars

#### Question 1
How can we access 256 MBit of data if there are only 13 address bits
- 2**13 = 8192 words.

### Micron: MT48LC16M16A2P-6A
- 4 Meg x 16 x 4: 256 MBit (32 MByte)
- 166 MHz
- 5.22 dollars
- TSSOP

### Micron MT48H16M32LFB-6
- MT48H16M32LFB5-6 IT:C TR
- 512 Mbit
- 4.95 dollars
- BGA package 
- Mobile LPSDR RAM

# Winbond: W9825G6KH-6
## Power
- Power supply: 3V3



## Symbol + footprint check
- PINS OK
- FOOTPRINT OK

# Examples
## Soldering Inkplate
Path: Soldered-Inkplate-MOTION-STM-board-hardware-design/CAD
### Decoupling Capacitance
- 2 x 1 uF
- 2 x 7 x 100 nF
- 2 x 10 nF
- 3 x 1 nF

### Ferrites
- None
- Vdd, vddq connected
## Icepi Zero

### Decoupling
- 7 x 22 nF
- 1 x 10 uF

### Ferrites
- None
- Vdd, vddq connected