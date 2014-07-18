from __future__ import unicode_literals
from __future__ import print_function

#Marco Forte, Counter
from PyDAQmx import *
import numpy as np
import ctypes

class Counter(Task):
    def __init__(self,deviceName = ""):
        self.name = ((deviceName if deviceName != "" else self.getDeviceName())+"/ctr0").encode('utf-8')
        Task.__init__(self)
        self.CreateCICountEdgesChan(self.name, b"", DAQmx_Val_Falling, 0, DAQmx_Val_CountUp)
    
    def start(self):
        self.StartTask()
        
    def stop(self):
        count = c_uint32()
        self.ReadCounterScalarU32(0,count, None)
        self.StopTask();
	
        return count.value
    
    def getCount(self):
        count = c_uint32()
        self.ReadCounterScalarU32(0,count, None)
        return count.value