#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

# Marco Forte, 19/06/2014

from counter import Counter
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

myCounter = Counter()
data = np.zeros(8)
rawData = []
for i in range(0, 10000):
    myCounter.start()
    sleep(0.01)

    count = myCounter.stop()

    # print(count)

    if i % 100 == 0:
        print(str(i) + ' counts')

    # data = [i+1 for i in data if count > i]

    rawData.append(count)
    data[count] = data[count] + 1.0

    # if( input("adjust voltage and continue, type exit to exit  ") == "exit"):
    #    break

print(np.var(rawData))
print(np.mean(rawData))
print(data)
f = open('rawCounterData.py', 'w')
f.write(repr(rawData))
f.close()
f = open('binnedCounterData.py', 'w')
f.write(repr(data))
f.close()
plt.hist(rawData, bins=6)
plt.show()

# print(myCounter.stop().value)
