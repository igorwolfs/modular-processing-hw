# Power
We need a way to select one of 3 power input source
- 3V3 through connector
- 5 V through USB VBUS
- 5 V through pins

## Power consumption
- MCU: < 200 mA
- SDRAM: 60 mA x 2 = 120 mA
- ADC frontend: 5 mA

So: 330 mA * 1.3 V = 430 mWatt max dissipation.

Use the AMS1117-3.3


## Solution
- Buck converter
- LDO
	- The power required here is not that high. 
	- An LDO should do the job if isolated enough.
	- Warning: 
		- The dropout voltage might be too high. So you must make sure that you have an ideal diode in parallel driving the load in case the input voltage is 3V3
			- Or maybe foresee 2 pins here

So TODO:
- 1 connection from vbus to LDO
- 1 connection from piezodriver-vin-connector to LDO (in case supply 5 V)

So 2x2 connector here:

- 1 connection from LDO to 3V3
- 1 connection from large vin-connector to 3V3 (in case)
- 1 connection from piezodriver-vin-connector to 3V3

So 3x2 connector here:

## Overvoltage protection
- Add a resettable overcurrent fuse
- Add reverse voltage breakdown protection
	- Choose SMF3.3CA for the input at 3V3
	- Choose SMF7.0CA for the input at 5V-6V

Diode package: SOD-123FL

### Package check
- Dimensions look good