# Buffer requirements
- GBW of at least 10 MHz

# Buffer examples
## INA333 (instrumentatino)
- BW: 150 kHz
- SR: 0.16 V/us
- Noise
	- @1kHz: 50 nV/sqrt(Hz)
- https://www.ti.com/lit/ds/symlink/ina333.pdf?ts=1760662953933

## OPA695 (precision)
- Good bandwidth
- More expensive

## AD8031
- GBW: 80 MHz
- SR: 30 V/us
- Price: 2+ euros
- Noise
	- @1kHz: 15 nV/sqrt(Hz)
- https://jlcpcb.com/api/file/downloadByFileSystemAccessId/8588901762816622592

## LTC6268
- Good bandwidth (500 MHz)
- Very low input impedance ()
- WAAAYY too expensive

## THS4521
- price: 0.8 $
- GBW: 145 MHz
- SR: 490 V/us
- Input voltage noise
	- > @10kHz
		- 4.6 nV/sqrt(Hz)
- Noise
	- @100 kHz: 
- Good option, bandwidth 40.7 MHz
- Maybe even a bit too much for our application


Seems like the best option
- The only thing that is quite shitty is the DC-offset for this one.

# THS4521
Images adc12, and adc3 were the resulting choices, some simulations can be found in the simulations/tina_ti folder that show the transfer function of these buffers with a dynamic load modelled after the stm32 parameters found in the datasheet.

