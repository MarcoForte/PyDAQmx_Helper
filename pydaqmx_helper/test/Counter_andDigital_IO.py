#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Tests digital IO and counter - and sends a sequence of o's and 1's on P0.0
and counts them.
Connect P0.0 to PFIO counter with a wire!
Should print out 666 
"""

from pydaqmx_helper.digital_io import Digital_IO
from pydaqmx_helper.counter import Counter
from time import sleep

myCounter = Counter()
myDigital_IO = Digital_IO()

myCounter.start()

for i in range(666):
    myDigital_IO.write(0)
    sleep(0.0001)
    myDigital_IO.write(1)
print(myCounter.stop())
