
# ADC (STM32H723ZGTx)
3 ADC's:
- 2 16 bits ADC's
	- ADC1, ADC2
	- Interleaved mode
	- Can work at 7.2 MHz
	- 16-bit ADC1 and ADC2 in double-interleaved mode at 7.2 MHz
	- 3/4 fast channels (PA6, PB1, PC4, PF11, PF13)
	- 11/12 slow channels
- ADC3 at 7.1 - 8.3 MSPS (12 bits)
	- 2 direct channels (PA0_C, PA1_C, PC2_C and PC3_C)
	- 6 fast channels

## Channel choice

3. Direct channels are connected to analog I/Os (PA0_C, PA1_C, PC2_C and PC3_C) to optimize ADC performance.
4. Fast channels correspond to PA6, PB1, PC4, PF11, PF13 for ADCx_INPx, and to PA7, PB0, PC5, PF12, PF14 for
ADCx_INNx.

Direct channels: connected to analog I/Os 
- PA0_C, PA1_C, PC2_C and PC3_C
	- So connect the 2 ADC's to one of these pins in interleaved mode
	- Choose PA0_C/PA1_C -> fast channel

Fast channels:
- PA6, PB1, PC4, PF11, PF13 for ADCx_INPx
- PA7, PB0, PC5, PF12, PF14 for ADCx_INNx
	- Connect the 3rd channel to one of the INPx pins
	- Choose PB0/1 -> fast channel

## Min / Max values


## Modelling
- Sample-and-hold capacitor: 4 pF
- Sampling time: 1.5-810.5 	times  1/f_adc
- Equivalent static impedance
	- Varies between 170 ohms and 26.5 kOhm
	- Table 78. Minimum sampling time vs RAIN (16-bit ADC)(1)(2) gives a more detailed image of the ADC input impedance

### Internal buffering
- The ADC requires an external on-chip buffer?
	- It does, the impedance of the signal will likely be too high, even coming from a buffering board.
	- So we'll go for an on-CPU differential-input ADC sampling

# ADC Model
## Connection diagram (Figure 38)
- $R_{ADC}$
- $C_{ADC}$
- $C_{parasitic}$: PCB capacitance + pad capacitance (4 pF)
- $R_{source}$

## Parasitics
### 12-bit ADC
- 