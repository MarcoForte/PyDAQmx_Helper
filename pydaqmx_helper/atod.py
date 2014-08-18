from __future__ import print_function

from PyDAQmx import *
import numpy as np
import ctypes
from itertools import *
from collections import OrderedDict



class AtoD(Task):
    
    """ Small class to provide simplified reading to the analog ports using PyDAQmx package."""

    def __init__(self, deviceName=""):
        self.name = (deviceName if deviceName != "" else self.getDeviceName()) + "/ai"
        Task.__init__(self)

    # def addChannel(self, channel,  AtoD_mode=DAQmx_Val_RSE,  minRange=-10.0,  MaxRange=10.0):
    #    self.CreateAIVoltageChan((self.name+str(channel)).encode('utf-8'), b"", AtoD_mode, minRange, MaxRange, DAQmx_Val_Volts, None)
    #   self.channelsNum = self.channelsNum + 1

    
    def sampleVoltages(self, nPointsPerChannel=1, sampleRate=1, channels=[]):
        """ Sample voltages at given rate from all channels,  default,  10,  10
        
        Attempts to add non active channels telling user
        Samples the voltage from all active channels
        Zips them up together with channel name and value into a dictionary
        Removes extra channels from dictionary that are not given active channels
        Orders the dictionary like given at beggining and returns ordered dictionary
          """  
        read = int32()

        activeChannels = self.getActiveChannels()

        sample = np.zeros(len(activeChannels)*nPointsPerChannel)
        self.CfgSampClkTiming(b"", sampleRate, DAQmx_Val_Rising, DAQmx_Val_FiniteSamps, 2 if nPointsPerChannel == 1 else nPointsPerChannel)
        self.StartTask()
        self.ReadAnalogF64(nPointsPerChannel, -1, DAQmx_Val_GroupByChannel, sample,  len(activeChannels)*nPointsPerChannel, byref(read), None)
        self.StopTask()
        sample = list(AtoD.grouper(sample, nPointsPerChannel))
        sample = OrderedDict(zip(activeChannels, sample))

        # Extracts wanted channels in order
        if(channels != []):
            newSample = dict()
            for key in sample:
                if (key in channels):
                    newSample[key] = sample[key]
            # Something like below could replace the above but it's not compatible between python 2 and 3
            # {key: value for (key, value) in sample.iteritems() if key in channels}
            return OrderedDict(sorted(newSample.items(),  key=lambda t: channels.index(t[0])))

        return sample

    
    def readVoltage(self):
        """ Read a floating-point voltage from a task with one channel"""
        voltage = c_double(0)
        self.ReadAnalogScalarF64(-1, voltage, None)
        return voltage.value

    
    def getActiveChannels(self):
        """ Return a python list of channel numbers

        At the end correctly extracts channel number from returned string of active channels
        """
        # Allocate space for channels,  simpler than getting exact right amount
        activeChannels = c_char_p(b"x"*300)
        self.GetTaskChannels(activeChannels, 300)
        if(activeChannels.value == b""):
            return []
        else:
            activeChannels = list(map(lambda x: int(x[-1]), activeChannels.value.decode('utf-8').split(',')))
            return activeChannels

    
    def addChannels(self, newChannels, AtoD_mode='DAQmx_Val_Diff', minRange=-10.0, maxRange=10.0):
        """ Add a list of channels with default settings or if given by user"""
        AtoD_mode = eval(AtoD_mode)
        for newChannel in newChannels:
            if(newChannel not in self.getActiveChannels()):
                self.CreateAIVoltageChan((self.name + str(newChannel)).encode('utf-8'), b"", AtoD_mode, minRange, maxRange, DAQmx_Val_Volts, None)
                print("Activated Channel " + str(newChannel))
    

    def grouper(iterable, n, fillvalue=None):
        """Collect data into fixed-length chunks or blocks"""
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)
