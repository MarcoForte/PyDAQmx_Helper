from __future__ import print_function

from PyDAQmx import *
import numpy as np
import ctypes
from itertools import *
from distutils.util import strtobool
from collections import OrderedDict

#Small class to provide simplified reading to the analog ports using PyDAQmx package.
class AtoD(Task):
    
    def __init__(self,deviceName=""):
        self.name = (deviceName if deviceName != "" else self.getDeviceName()) + "/ai"
        Task.__init__(self)
        self.channelsNum = 0

    #def addChannel(self,channel, AtoD_mode=DAQmx_Val_RSE, minRange=-10.0, MaxRange=10.0):
    #    self.CreateAIVoltageChan((self.name+str(channel)).encode('utf-8'),b"",AtoD_mode,minRange,MaxRange,DAQmx_Val_Volts,None)
    #   self.channelsNum = self.channelsNum + 1
     
     #Samples voltages at given rate from all channels, default, 10, 10
     # Multiple Channels
        #   Attempts to add non active channels warning user
        #   Samples the voltage from all active channels
        #   Zips them up together with channel name and value into a dictionary
        #   Removes extra channels from dictionary that are not given active channels
        #   Orders the dictionary like given at beggining and returns ordered dictionary
    def sampleVoltages(self,nPointsPerChannel = 1, sampleRate = 1,*channels):
        read = int32()
      
       
        requestedActiveChannels  = self.addChannels(*channels)
        
        sample = numpy.zeros(self.channelsNum*nPointsPerChannel)
        
        self.CfgSampClkTiming(b"",sampleRate,DAQmx_Val_Rising,DAQmx_Val_FiniteSamps, 2 if nPointsPerChannel == 1 else nPointsPerChannel)
        self.StartTask()
        self.ReadAnalogF64(nPointsPerChannel,-1,DAQmx_Val_GroupByChannel,sample, self.channelsNum*nPointsPerChannel,byref(read),None)
        self.StopTask()
        sample = list(AtoD.grouper(sample,nPointsPerChannel))
        sample = OrderedDict(zip(self.getActiveChannels(),sample ))
        
        if(requestedActiveChannels != []):
            newSample = dict()
            for key in sample:
                if (key in requestedActiveChannels):
                    newSample[key] = sample[key]
            return OrderedDict(sorted(newSample.items(), key=lambda t: requestedActiveChannels.index(t[0])))
        
        return sample
        
        
    #Reads floating-point voltage from a task with one channel
    def readVoltage(self):
        voltage = c_double(0)
        self.ReadAnalogScalarF64(-1,voltage,None)
        return voltage.value
        
    # Returns python list of channel numbers
    # At the end correctly extracts channel number from returned string of active channels
    def getActiveChannels(self):
        #Allocate space for channels, simpler than getting exact right amount
        activeChannels =  c_char_p(b"x"*300)
        self.GetTaskChannels(activeChannels,300)
        if(activeChannels.value == b""):
            return []
        else:
            activeChannels = list(map(lambda x:int(x[-1]) ,activeChannels.value.decode('utf-8').split(',')))
            return activeChannels
        
    
    
        
    ##### Adds multiple channels and returns from the inputted list those channels which are now active
    # removes duplicates and puts channels given into a list
    # loops through activating channels and depending on checkAdd asks the user or not to do so
    def addChannels(self, *channels, AtoD_mode=DAQmx_Val_Diff, minRange=-10.0, maxRange=10.0):
        activeChannels = self.getActiveChannels()
        currentChannels = []
        for channel in channels :
            if(channel not in activeChannels):
                self.CreateAIVoltageChan((self.name+str(channel)).encode('utf-8'),b"",AtoD_mode,minRange,maxRange,DAQmx_Val_Volts,None)
                self.channelsNum = self.channelsNum + 1
                currentChannels.append(channel)
                print("Activated Channel " + str(channel))
            elif(channel not in currentChannels):
                currentChannels.append(channel)
        return currentChannels
       
    def grouper(iterable, n, fillvalue=None):
        "Collect data into fixed-length chunks or blocks"
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)