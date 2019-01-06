#!/usr/bin/env python

import json
import urllib2
import urllib
import time
import blinkt

blinkt.set_clear_on_exit()

test_url = "https://www.spiegel.de"
api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
           urllib.quote_plus(test_url) + \
           "&category=accessibility&category=best-practices&category=performance&category=pwa&category=seo&strategy=mobile"



def setPixelFromJson(pixel, json, path):
        obj = json;
        while len(path) > 0:
            key = path.pop(0)
            obj = obj[key]
        if obj > 0.75:
           blinkt.set_pixel(pixel, 0, 255, 255)
        elif obj > 0.5:
           blinkt.set_pixel(pixel, 150, 150, 0)
        else:
           blinkt.set_pixel(pixel, 255, 0, 0)




while True:
    print  "new run"
    print "query lighthouse"
    report = json.load(urllib2.urlopen(api_url))
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
