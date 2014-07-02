# Marco Forte, 18/06/2014
# Example program to show how to read multiple
# samples from a single AtoD channel with a 
# user-specified range at a given sample rate

from AtoD import *

myAtoD = AtoD()
myAtoD.addChannels(0,AtoD_mode=DAQmx_Val_Diff,minRange=-5.0,maxRange=5.0)
# samplevoltages returns a dictionary with voltages and channels as key value pairs.
# Here we get the values from channel 0 
samples = myAtoD.sampleVoltages(50,10)[0]
size = len(samples)
for i in range(size):
    print(samples[i])
 