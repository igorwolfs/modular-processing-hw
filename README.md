# MCU-BOARD


## Acoustic-carrier Project
The goal is to design a small CPU board, with some RAM and connectors, that can
- Drive the piezo-driver / inverter board
- Save about 1 second of data from 2 30 MHz ADC's
	- Reflection at origin-piezo
	- Transmission from origin to second-piezo
- Processing of the data on the MCU in the next few seconds
- Storage of the processed data on an SD-CARD
- Transmission of the processed data over Hi-Speed USB / Ethernet to a computer
