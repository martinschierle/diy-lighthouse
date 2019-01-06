#!/usr/bin/env python

import json
import urllib2
import time
import blinkt

blinkt.set_clear_on_exit()

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fwww.spiegel.de&category=accessibility&category=best-practices&category=performance&category=pwa&category=seo&strategy=mobile"

while True:
    print  "new run"
    print "query lighthouse"
    report = json.load(urllib2.urlopen(url))
    print "Result: " + str(report['lighthouseResult']['audits']['metrics']['det$
    blinkt.set_pixel(i, 255, 150, 0)
    blinkt.show()
    time.sleep(0.1)
