# Do-It-Yourself Lighthouse

This is a small overview on how to build a little Lighthouse object with a RaspberryPi Zero, which will show Lighthouse scores for a given website via a set of URLs

# Partlist
* RaspberryPi Zero with Male headers (e.g. [here](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header))
* Blink LED line ([here](https://shop.pimoroni.com/products/blinkt))
* Micro-USB wall charger (if needed, should be 1A)
* SD card (8GB)


# Instructions
* Install Raspbian on SD card (see e.g. [here](https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/))
* Log into Raspi
* Install BLinkt library (see [here](https://github.com/pimoroni/blinkt))
** Basicall just run: 
** curl https://get.pimoroni.com/blinkt | bash
* Copy lighthouse.py from this repository to the home dir (e.g. via copy&paste)
