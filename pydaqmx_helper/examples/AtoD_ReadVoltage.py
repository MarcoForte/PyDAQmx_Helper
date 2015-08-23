from __future__ import print_function
"""
Example program to show how to read from a single AtoD channel with default settings
Should print out the correct voltage value for channel 0
"""

from pydaqmx_helper.atod import AtoD

myAtoD = AtoD()
myAtoD.addChannels([0])
val = myAtoD.readVoltage()
print(val)
