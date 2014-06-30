# Marco Forte, 18/06/2014
# Example program to show how to read multiple
# samples from multiple AtoD channels at a given sample rate
from AtoD import *

myAtoD = AtoD()
myAtoD.addMultipleChannels(0,1,2)
sample = myAtoD.readVoltage(2,1)
print(sample)
print(list(sample.values()))