#Marco Forte, Counter
from PyDAQmx import *
import numpy as np
import ctypes

class Counter(Task):
    def __init__(self):
        self.name = bytes(self.getDeviceName()+"/ctr0",'utf-8')
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