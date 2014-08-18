from __future__ import print_function

# Marco forte,  Digital IO,  especially designed for USB6008
from PyDAQmx import *
import numpy as np
import ctypes


class Digital_IO(Task):

    """ Inherits the task class, and simplifies digital_IO work
    Supports reading and writing to channels 0, 1 or 0 and 1
    """
    
    def __init__(self, port="0:1",  direction="output", deviceName=""):
        self.port = port
        self.name = ((deviceName if deviceName != "" else self.getDeviceName()) + "/port" + str(port)).encode('utf-8')
        self.direction = str(direction)
        Task.__init__(self)

        if(self.direction == "input"):
            self.CreateDIChan(self.name, b"", DAQmx_Val_ChanForAllLines)
        else:
            self.CreateDOChan(self.name, b"", DAQmx_Val_ChanForAllLines)
        print("Created digital " + self.direction + " port: " + self.name.decode('utf-8'))

    def write(self, num):
        """ Convert num to binary string with leading zeros, depends on port '0:1' or '0'/'1'
    
        Convert binary string to numpy array using list comprehensions
        Note on the below,[len(ui16):2:-1], binary reversal, done to match up intuitively with ports on usb6008
        """
        if(self.direction != "output"):
            print("Ports are not set as output, please set them to output to be able to write ")
            return None

        if self.port == "0:1":
            num = num & 4095
            binaryNum = format(num, '#014b')
        elif self.port == "0":
            num = num & 255
            binaryNum = format(num, '#010b')
        else:
            num = num & 15
            binaryNum = format(num, '#06b')

        #binaryNum = (format(num, '#018b') if self.port == "0:1" elif self.port == "0"  else format(num, '#06b'))
        #data = np.array([int(i) for i in binaryNum[len(binaryNum):2:-1]], dtype='uint8')
        #self.WriteDigitalLines(1, 1, 10.0, DAQmx_Val_GroupByChannel, data, None, None)
        self.WriteDigitalScalarU32(True, -1, ctypes.c_uint32(num), None)
        return binaryNum


    def read(self):
            """ Read a voltage from the port given to the constructor
            Creates empty array to read into
            Reads in digital port(s)
            converts sampled reading to binary and uses min number of lower bits
            """
            if(self.direction != "input"):
                print("Ports are not set as input, please set them to input to be able to write ")
                return 0
            sample = ctypes.c_ulong(4095)
            
            self.ReadDigitalScalarU32(10, sample, None)
            if(self.port == "1"):
                return format(sample.value & 15, '#06b')
            elif(self.port == "0:1"):
                return format(sample.value & 4095, '#14b')
            else:
                return format(sample.value & 255, '#10b')

