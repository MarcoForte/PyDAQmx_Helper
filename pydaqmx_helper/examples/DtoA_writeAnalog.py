#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

""" Example program to show how to write a single
2.62v voltage to the first DtoA channel. """

from pydaqmx_helper.dtoa import DtoA
myDtoA = DtoA(0)
myDtoA.writeVoltage(2.62)
