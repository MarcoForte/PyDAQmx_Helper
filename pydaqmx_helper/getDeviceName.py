from PyDAQmx.DAQmxFunctions import *

def getDeviceName():
	a = c_char_p(b' ')
	# Buffer will break if too many devices, like 10 or 15, make number 100 bigger if you have to
	b = c_ulong(100)
	DAQmxGetSysDevNames(a, b)
	return a.value.decode('utf-8').split(',')[-1].strip()