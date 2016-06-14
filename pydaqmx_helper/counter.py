from __future__ import unicode_literals
from __future__ import print_function

# Marco Forte, Counter
from PyDAQmx import *
import numpy as np
import ctypes
from pydaqmx_helper.getDeviceName import getDeviceName

class Counter(Task):

    """ Inherits the task class, and simplifies counter work
    Supports stop and starting the counters and also getting a running count
    """
    
    def __init__(self, deviceName=""):
        self.name = ((deviceName if deviceName != "" else getDeviceName())+"/ctr0").encode('utf-8')
        Task.__init__(self)
        self.CreateCICountEdgesChan(self.name, b"", DAQmx_Val_Falling, 0, DAQmx_Val_CountUp)

    def start(self):
        self.StartTask()

    def stop(self):
        """ Stop the counter and return the count"""
        count = c_uint32()
        self.ReadCounterScalarU32(0, count, None)
        self.StopTask()
        return count.value

    def getCount(self):
        """ Return a count without stoppping the counter """
        count = c_uint32()
        self.ReadCounterScalarU32(0, count, None)
        return count.value
