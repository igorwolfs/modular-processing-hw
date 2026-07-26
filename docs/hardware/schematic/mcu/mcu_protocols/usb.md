# USB
- a USB-pull-up resistor should be internal
	- Check reference schematic for nucleo
	- Check application ntoe

# SWD
- SWD-bus has no pull-ups present on the nucleo board.
- SWD-bus has both pull-ups and pull-downs present.
	- NJTRST: internal PU
	- SWDIO: pu
	- SWCLK: pd