# MCU
## STM32
- LPN: ok
- MPN: ok

### Schematic
- Pins OK -> Compared with output on footprint vs STM32 output
- Make still check BS0/BS1 for wrong outputs

### Footprint
- Check footprint dimensions
	- Looks good


## Resonator
- LPN: ok
- MPN: ok

### Schematic
- pin2, 4 -> GND
- pin 1, 3: connected to res
	- 4.7 pF capacitors

### Footprint
- Looks good

## Button
- LPN: ok
### Footprint
- ok

# SDRAM
## BA / BS
and bank address (BA), also
known as bank select (BS).

## Schematic
- Connections look ok

## Footprint
- Check pin number vs Symbol number
- Footprint: 
	- Package_SO:TSOP-II-54_22.2x10.16mm_P0.8mm
- SDRAM looks ok

# USB
## USB Receptacle
- USB_C_Receptacle_HRO_TYPE-C-31-M-12
- Looks good (footprints + pinout)

## USB ESD protection

- Package_TO_SOT_SMD:SOT-23-6

## Resistive pull-up
- Resistor_SMD:R_Array_Convex_4x0603
- Footprint: ok

## SDMMC
### Schematic
- pins vs footprint:

### Footprint

### Layout
TODO:
- Keep skew below 10 mm
- Add pull-up on cmd line?
	- CMD line must have pull-up as well
	- https://community.st.com/t5/stm32-mcus-products/using-sdmmc-sdio-and-fatfs-for-reading-sd-card-for-stm32l471vgt6/td-p/689667

DONE

## Connectors
- Plug_Hirose_DF40_2x40_DF40C-80DP-0.4V (DF40C-80DP-0.4V(51))
- Footprint: iw-connector:HRS_DF40C-80DP-0.4V(51)

### Footprint
- Looks correct -> number of pins is also correct
- Pin indicators (uneven / even), instead of counting as in jlc -> but ok

# ADC Frontend
- Reference buffering: checked, should work
## THS4521
- Looks ok
- Pins: ok
### Footprint: ok

## Everything else: looks ok

# Power
- AMS1117-3.3: looks ok

## Footprint package: looks OK

## SDRAM length matching

### First connection
- CLK: 38.7 mm
- A0..A12
	- A0: 46
	- A1: 46
	- A2: 47
	- A3: 47.9
	- A4: 40.3
	- A5: 36 mm
	- A6: 40.9 
	- A7: 39
	- A8: 35
	- A9: 34
	- A10: 44
	- A11: 34
	- A12: 35
- BS0..1: 
	- BS1: 34
	- BS0: 33
-> ALL OK
- D0..16
	- D0: 38.7
	- D1: 32
	- D2: 41
	- D3: 42
	- D4: 36.3
	- D5: 35
	- D6: 37
	- D7: 36.3
	- D8: 31
	- D9: 30
	- D10: 30
	- D11: 30.5
	- D12: 30.5
	- D13: 34
	- D14: 31.6
	- D15: 32.8
- Other
	- nRAS: 48
	- nCAS: 44
	- nWE: 47
	- LDQM: 47.5
	- UDQM: 37.2
	- nCKE0: 49

### Second connection
- CLK: 68 mm
- A0..A12
	- A0: 71.8
	- A1: 72
	- A2: 72
	- A3: 73
	- A4: 64
	- A5: 66
	- A6: 63
	- A7: 63
	- A8: 60
	- A9: 66
	- A10: 68
	- A11: 62
	- A12: 65
- BS0..1: 
	- BS1: 69
	- BS0: 66
- D0..16
	- D0: 64
	- D1: 62
	- D2: 69
	- D3: 66
	- D4: 62
	- D5: 61
	- D6: 61
	- D7: 60.3
	- D8: 60
	- D9: 60
	- D10: 62
	- D11: 65
	- D12: 63
	- D13: 66
	- D14: 61.3
	- D15: 61
- Other
	- nRAS: 74
	- nCAS: 68
	- nWE: 73
	- LDQM: 73
	- UDQM: 65
	- nCKE1: 65

## PSSI length matching
- PDCK: 34 mm
- D8: 56.3 mm
- D12: 54 mm
- D13: 51 mm
- D6, D7: 17 mm

Increase PDCK to 45 mmm
- Match everything to +-15 mm

## SDMMC length
- D0..D3
	- D0: 76
	- D1: 81
	- D2: 83
	- D3: 85
- CD: 88
- CMD: 81

# Differential Impedances
- ADC: OK
- USB: OK

