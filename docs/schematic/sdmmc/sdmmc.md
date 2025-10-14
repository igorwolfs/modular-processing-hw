# SDMMC


## Hardware design
### Pull-ups / downs
- CMD + DATA[0..3] lines must be pulled up by 10 kOhm resistors
	- https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/sd_pullup_requirements.html
	