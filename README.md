# Do-It-Yourself Lighthouse

This is a small overview on how to build a little Lighthouse object with a RaspberryPi Zero, which will show Lighthouse scores for a given website via a set of LEDs

![Finished built](https://raw.githubusercontent.com/martinschierle/diy-lighthouse/master/lighthouse_built1.jpg)

# Partlist
* RaspberryPi Zero with Male headers (e.g. [here](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header))
* Blink LED line ([here](https://shop.pimoroni.com/products/blinkt))
* Micro-USB wall charger (if needed, should be at least 1A)
* SD card (8GB)


# Instructions
* Install Raspbian on SD card (see e.g. [here](https://thepi.io/how-to-install-raspbian-on-the-raspberry-pi/))
* Log into Raspi
    * you can do this by connecting monitor, mouse and keyboard, but that's cumbersome (the zero needs quite some adapters)
    * Easier:
        * Open hotspot on phone
        * Create wpa_supplicant.conf with wifi password and copy to sd card root (see [here](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/))
        * Create an empty file called ssh (no extension) and copy it to sd card root (to enable ssh, see [here](https://www.raspberrypi.org/forums/viewtopic.php?t=167326))
        * Boot up zero, it should connect to wifi automatically
        * SSH in via e.g. Putty, using the default hostname/user/password (raspberrypi/pi/raspberry)
* Do settings as you see need via [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
    * You might wanna change username, password, hostname, language/locale
* Install Blinkt library (see [here](https://github.com/pimoroni/blinkt))
    * Basicall just run: 
    * curl https://get.pimoroni.com/blinkt | bash
* Copy lighthouse.py from this repository to the home dir (e.g. via copy&paste)
* Run once to make sure it works
    * Adapt test_url to your needs
    * Script starts with a quick moving rainbow to signal succesful start
    * On the first run it will afterwards signal the IP via the leds. Numbers from 0 to 8 are blue leds, a line of red leds means the dot, a 9 is 7 blue dots plus a green one. So '192.168.1.1" would be 1 blue, 7blue+1green,2 blue, all red, 1 blue, 6 blue, 8 blue, all red, 1 blue, all red, 1 blue
* Add lighthouse.px to autostart as described [here](https://stackoverflow.com/questions/24875955/autostart-on-raspberry-pi)
    * Basically add 'python /home/pi/lighthouse.py' to /etc/rc.local
* Build it up
    * Print the frontcover.svg file from this repo to A4 paper
    * Cut out the black bar in the middle (and label the space besides it with whatever metrics you end up displaying like 'FCP')
    * Do the two cuts on the upper and the two cuts on the lower end
    * Cut off the upper line of paper
    * Bend the line of paper and insert it into the two bottom cuts as a foot to the lighthouse
    * Also bend the left and right border of the paper as well to get more stability
    * Attach blinkt led bar to raspbery zero through the cutout in the middle, connect power
    * You're done!

# For events/hackathons
If you need many of these for events, you have two options:
* Get the raw materials and let all participants follow the steps above (needs more time, more error prone)
* Do the setup once (with wifi configured to your event space, you can also [configure several](https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks)) yourself, and then clone the sd card several times (e.g. directly from [raspberry UI](https://pishop.co.za/blog/my-tutorial-post/clone-your-micro-sd-directly-on-rpi/))
