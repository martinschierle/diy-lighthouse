#!/usr/bin/env python

import json
import urllib2
import urllib
import time
import blinkt
import colorsys
import time
import subprocess

blinkt.set_brightness(0.08)
blinkt.set_clear_on_exit()

first = True
test_url = "https://www.stern.de"
api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
           urllib.quote_plus(test_url) + \
           "&category=accessibility&category=best-practices&category=performance&category=pwa&category=seo&strategy=mobile"


def showRainbow(duration):
    showing = 0
    spacing = 360.0 / 16.0
    hue = 0
    while showing < duration:
        hue = int(time.time() * 100) % 360
        for x in range(blinkt.NUM_PIXELS):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            blinkt.set_pixel(x, r, g, b)

        blinkt.show()
        time.sleep(0.01)
        showing += 0.01

def showNumber(n):
    if n.isdigit():
        no = int(n)
        if no <= blinkt.NUM_PIXELS:
            for x in range(no):
                blinkt.set_pixel(x, 0, 0, 255)
        else:
            for x in range(blinkt.NUM_PIXELS-1):
                blinkt.set_pixel(x, 0, 0, 255)
            blinkt.set_pixel(blinkt.NUM_PIXELS-1, 0, 255, 0)
    else:
        for x in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(x, 255, 0, 0)
    blinkt.show()
    time.sleep(1)
    blinkt.clear()
    blinkt.show()
    time.sleep(0.5)


def setPixelFromJson(pixel, json, path):
    obj = json;
    while len(path) > 0:
        key = path.pop(0)
        obj = obj[key]
    # score above 75% is green
    if obj > 0.75:
       blinkt.set_pixel(pixel, 0, 239, 23)
    # score above 50% is orange
    elif obj > 0.5:
       blinkt.set_pixel(pixel, 239, 147, 0)
    # else score is red
    else:
       blinkt.set_pixel(pixel, 255, 0, 0)




while True:
    # indicate that we refresh results by showing a rainbow for some seconds
    showRainbow(3)
    blinkt.clear()
    blinkt.show()
    try:
        print "query lighthouse"
        report = json.load(urllib2.urlopen(api_url))
    except urllib2.URLError:
        print "Not Connected, retrying in 10sec"
        time.sleep(10)
    else:
        # after first successfull network connection show the IP quickly through the leds
        if first:
            ip = subprocess.check_output(["hostname", "-I"]).split()[0]
            for c in str(ip):
                showNumber(c)
            first = False
        # now show lighthouse results
        lhr = report['lighthouseResult']
        setPixelFromJson(0, lhr, ['audits', 'first-contentful-paint', 'score'] )
        setPixelFromJson(1, lhr, ['audits', 'first-meaningful-paint', 'score'] )
        setPixelFromJson(2, lhr, ['audits', 'speed-index', 'score'] )
        setPixelFromJson(3, lhr, ['audits', 'first-cpu-idle', 'score'] )
        setPixelFromJson(4, lhr, ['audits', 'interactive', 'score'] )
        setPixelFromJson(5, lhr, ['categories', 'performance', 'score'])
        setPixelFromJson(6, lhr, ['categories', 'pwa', 'score'])
        setPixelFromJson(7, lhr, ['categories', 'seo', 'score'])
        blinkt.show()
        # update in 10min
        time.sleep(600)
