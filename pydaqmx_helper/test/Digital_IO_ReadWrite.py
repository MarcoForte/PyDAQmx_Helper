from pydaqmx_helper.digital_io import Digital_IO
from pydaqmx_helper.counter import Counter
import ctypes

""" Connect P0.0 and P1.0
Should print out 14
"""
dout = Digital_IO("0")
dout.write(0)

din = Digital_IO("1", "input")
print(str(din.read()))
