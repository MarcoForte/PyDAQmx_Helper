#Marco forte Digtial to Analog, top-level simplified interface
from PyDAQmx import *
import numpy as np
import ctypes

class DtoA(Task):
    
    def __init__(self,channel):
        
        self.name = bytes(self.getDeviceName()+"/ao"+str(channel),'utf-8')
        Task.__init__(self)
        self.CreateAOVoltageChan(self.name,b"",0.0,5.0,DAQmx_Val_Volts,None)

    
    def writeVoltage(self,voltage):
        sample = np.ones(1)*voltage
        self.StopTask()
        self.StartTask()
        self.WriteAnalogF64(1,1,10.0,DAQmx_Val_GroupByChannel,sample,None,None)
        self.StopTask()
       