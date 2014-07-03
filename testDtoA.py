# Marco Forte, 18/06/2014
# Example program to show how to write a single 
# voltage to the first DtoA channel.

from dtoa import DtoA
myDtoA = DtoA(0)
myDtoA.writeVoltage(2.62)

