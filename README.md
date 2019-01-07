# Do-It-Yourself Lighthouse

This is a small overview on how to build a little Lighthouse object with a RaspberryPi Zero, which will show Lighthouse scores for a given website via a set of LEDs

# Partlist
* RaspberryPi Zero with Male headers (e.g. [here](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header))
* Blink LED line ([here](https://shop.pimoroni.com/products/blinkt))
* Micro-USB wall charger (if needed, should be at least 1A)
* SD card (8GB)


# Instructions
* Install Raspbian on SD card (see e.g. [here](https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/))
* Log into Raspi
** you can do this by connecting monitor, mouse and keyboard, but that's cumbersome (the zero needs quite some adapters)
** Easier:
*** Open hotspot on phone
*** Create wpa_supplicant.conf with wifi password and copy to sd card root (see [here](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/))
*** Boot up zero, it should connect to wifi automatically
*** SSH in via e.g. Putty, using the default hostname/user/password (raspberrypi/pi/raspberry)
* Do settings as you see need via [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
** You might wanna change username, password, hostname, language/locale
* Install BLinkt library (see [here](https://github.com/pimoroni/blinkt))
** Basicall just run: 
** curl https://get.pimoroni.com/blinkt | bash
* Copy lighthouse.py from this repository to the home dir (e.g. via copy&paste)
* Run once to make sure it works
** Adapt test_url to your needs
* Add lighthouse.px to autostart as described [here](https://stackoverflow.com/questions/24875955/autostart-on-raspberry-pi)

# For events/hackathons
If you need many of these for events, you have two options:
* Get the raw materials and let all participants follow the steps above (needs more time, more error prone)
* Do the setup once (with wifi configured to your event space, you can also [configure several](https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks)) yourself, and then clone the sd card several times (e.g. directly from [raspberry UI](https://pishop.co.za/blog/my-tutorial-post/clone-your-micro-sd-directly-on-rpi/))
