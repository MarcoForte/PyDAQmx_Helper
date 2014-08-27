#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Read out counts while task is running
Simlarly to testcounter_andDigital_IO.py it should print out 666
But this also prints out every 10 counts
"""

from pydaqmx_helper.digital_io import Digital_IO
from pydaqmx_helper.counter import Counter
from time import sleep

myCounter = Counter()
myDigital_IO = Digital_IO()

myCounter.start()

for i in range(666):
    if i % 10 == 0:
        print(myCounter.getCount())
    myDigital_IO.write(0)
    sleep(0.0001)
    myDigital_IO.write(1)
print(myCounter.stop())
