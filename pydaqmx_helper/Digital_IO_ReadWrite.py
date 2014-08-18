from digital_io import Digital_IO
from pydaqmx_helper.counter import Counter
import ctypes
# Connect P0.0 and P1.0
# Should print out 1100
dout = Digital_IO("0")
dout.write(0)

din = Digital_IO("1", "input")
print(str(din.read()))
buffer = ctypes.c_uint32(0)

din.ReadDigitalScalarU32(-1, buffer, None)
print(str(buffer))