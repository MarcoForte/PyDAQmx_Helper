# Example program to show how to read from a single AtoD channel with default settings
# Marco Forte, 18/06/2014

from AtoD import *

myAtoD = AtoD()
myAtoD.addChannel(0)
val = myAtoD.readVoltage()
print(val)