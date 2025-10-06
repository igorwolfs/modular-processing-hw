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

### Internal ADC
- Single / dual channel ADC

### Alternative
- Downsampling / decimation of ADC data before in small DSP CPU

## USB
- ULPI interface

## SDRAM
- Data transfer:
	- 30 MHz x 2 bytes -> 57.3 Mbytes / second
	- Should be able to save at least a second of data

## Ethernet
- RGMII interface

## DSP
- Full DSP instruction set