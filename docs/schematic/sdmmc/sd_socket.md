# The SD Socket
The SD card socket has 4 pads on the metal shielding and 11 pinouts (also pads, at the back). An online search reveals that the pinouts of these components are fairly standard. That’s understandable given the fungible / standardized nature of the cards themselves.

Many of the pins simply connect directly through to the pads of the SD card itself. So let’s consider those:

- DAT3 / CS
- CMD / DI
- VSS1
- VCC
- CLK / SCLK
- VSS2
- DAT0 / DO
- DAT1
- DAT2

The very small microSD cards have only 8 pins. On those there is only one VSS pin.

To these, the SD card slot adds three pins:

- Card Detect (CD)
- Common Switch
- Write Protect (WP)

Note: only eight of the pins are used in this project.

## Power Pins
Pins VSS1, VSS2 and VCC relate to power supply.

### Vss
VSS stands for voltage source and is where ground should be connected. On other schematics it may be labelled as GND.

### Vdd
VDD stands for voltage drain and is where positive power should be connected. On other schematics it may be labelled as VCC, which stands for voltage collector.

## Data Pins

SD cards can be operated in SPI (serial peripheral interface) mode or native operating mode. Because the SD card can be attached to most microcontrollers via a generic SPI interface or some GPIO ports it is a suitable for many projects. Therefore we will discuss pins as they are used in this mode.

### SPI 
The SPI protocol defines a host and slave relationship, described at http://elm-chan.org/docs/spi_e.html 105. This is important to remember in the reading of the pins below. Also, throughout these notes I use the terms host and microcontroller interchangeably.

### DAT3 / CS

This is the Data 3 pin in native mode and Chip Select pin in SPI mode. It is used by the SPI host (in our case, the microcontroller) to indicate that it’s communicating with the slave. It can also be used by the slave to indicate to the host it is ready to communicate.

This functionality means the data out and data in pins can be part of a shared data bus (with other SPI slave devices on it).

### CMD / DI
This is the Command pin in native mode and Data In pin in SPI mode. It is used by the SPI host to send serial data (bit by bit) to the SD card (the slave) and is sometimes referred to as Master-Out Slave-In (MOSI).

### DAT0 / DO
This is the Data 0 pin in native mode and Data Out pin in SPI mode. It is used by the SPI slave to send serial data (bit by bit) to its host (the microcontroller) and is sometimes referred to as Master-In Slave-Out (MISO).

### CLK / SCLK
This is the Clock pin in both modes. It is used by the SPI host to provide a clock pulse for the purposes of sending and receiving data on the DI and DO pins.

## Card Slot Pins
### Card Detect (CD)

This pin is used to detect whether a card has been inserted in the slot. The mechanism by which this is done seems common across slot models (based on a random sampling of datasheets available online): the pin is connected to a mechanical switch which closes when the card is inserted and connects to ground on the other side. On the one we are using, the switch mechanism is exposed and clearly visible on the top of the slot (in the cut-away section of the shielding). Insert a card and you will see how the bent piece of metal (part of the shielding) touches another piece of metal. You can use a multimeter to test that the second piece of metal is connected to the CD pin and the bent piece (and indeed the entire shielding) is connected to ground.

To use the card detect functionality you would connect the CD pin to a positive power rail via a pull-up resistor so that you get a high signal when the slot is empty and a low signal when a card is inserted. This functionality is not used in this project.

This pin is also connected to the Common pin when a card is inserted and disconnected from the Common pin when there is no card inserted. This is an alternative way of using the pin.

### Write Protect (WP)
This pin is used to detect whether an inserted card has got Write Protect enabled. As with the CD pin, this is connected to ground when a card is inserted Write Protect on and you would need to have it pulled-up in order to use it.

As with the CD pin, this pin is connected to the Common pin when Write Protect is inserted and otherwise disconnected from the Common pin.

### Common Switch
Both the CD and WP pins above are connected to this pin, in addition to ground, when they are activated, providing another way for us to implement that functionality.

# Source:
- https://community.circuitmess.com/t/understanding-the-sd-card-slot/2801