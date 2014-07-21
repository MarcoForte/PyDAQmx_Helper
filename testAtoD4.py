#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Marco Forte, 19/06/2014
# Read in analog signal from 1 channel and plot it
# using oscilloscope, ramp or sine 2.2Hz, 1.41Vpp get good picture
#

import numpy
import matplotlib.pyplot as plt

from atod import AtoD

myAtoD = AtoD()
myAtoD.addChannels([0])

data = list(myAtoD.sampleVoltages(100, 100)[0])

x = numpy.arange(100)
print(numpy.average(data))
plt.plot(x, data)
plt.show()
