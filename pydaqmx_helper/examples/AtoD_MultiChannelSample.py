#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Marco Forte, 18/06/2014
# Example program to show how to read multiple
# samples from multiple AtoD channels at a given sample rate

from pydaqmx_helper.atod import AtoD

myAtoD = AtoD()
myAtoD.addChannels([0, 1, 2])
sample = myAtoD.sampleVoltages(10, 10, [2, 1])
print(sample)
print('Printing just values ')
print(list(sample.values()))
