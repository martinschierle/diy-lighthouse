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
* Do settings as you see need via [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
** You might wanna change username, password, hostname, language/locale
* Install BLinkt library (see [here](https://github.com/pimoroni/blinkt))
** Basicall just run: 
** curl https://get.pimoroni.com/blinkt | bash
* Copy lighthouse.py from this repository to the home dir (e.g. via copy&paste)
* Run once to make sure it works
** Adapt test_url to your needs
* Add lighthouse.px to autostart as described [here](https://stackoverflow.com/questions/24875955/autostart-on-raspberry-pi)
