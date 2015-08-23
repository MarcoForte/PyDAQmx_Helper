#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
# Block below for Python 2&3 support
try:
    input = raw_input
except NameError:
    pass

""" Example of using Digital IO to  write across both ports 0 and 1 of the Usb 6008"""

from pydaqmx_helper.digital_io import Digital_IO

myDigital_IO = Digital_IO()
while True:
    inputNum = input('Enter number to write: (Enter nothing to exit)')
    if not inputNum.isdigit():
        print('Input, ' + inputNum + ' ,not a number, exiting...')
        break

    myDigital_IO.write(int(inputNum))
