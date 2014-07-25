#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass
# Marco Forte, 18/06/2014
# Test Digital IO by writing across both ports 0 and 1 of the Usb6008

from digital_io import Digital_IO

# Default options are output and

myDigital_IO = Digital_IO()
while True:
    inputNum = input('Enter number to write: (Enter nothing to exit)')
    if not inputNum.isdigit():
        print('Input, ' + inputNum + ' ,not a number, exiting...')
        break

    myDigital_IO.write(int(inputNum))
