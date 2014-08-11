#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Marco Forte, 18/06/2014
# Example program to show how to read multiple
# samples from a single AtoD channel with a
# user-specified range at a given sample rate
# Should print out 50 samples

from pydaqmx_helper.atod import AtoD

myAtoD = AtoD()
myAtoD.addChannels([0], AtoD_mode=DAQmx_Val_Diff, minRange=-5.0,
                   maxRange=5.0)

# Returns a dictionary with voltages and channels as key value pairs.
# Here we get the values from channel 0

samples = myAtoD.sampleVoltages(50, 10)[0]
for sample in samples:
    print(sample)
