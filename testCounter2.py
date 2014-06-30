# Marco Forte, 19/06/2014
from Counter import *
from time import sleep
import matplotlib.pyplot as plt 
import numpy as np

myCounter = Counter()
data = np.zeros(30)
rawData = []
for i in range(0,1000):
    myCounter.start()
    sleep(0.05)
    
    count = myCounter.stop()
    if(i % 100 == 0):
        print(str(i) + " counts")
    #data = [i+1 for i in data if count > i]
    rawData.append(count)
    data[count] = data[count] + 1.0
   # if( input("adjust voltage and continue, type exit to exit   ") == "exit"):
    #    break

print(np.var(rawData))
print(np.mean(rawData))
print(data)
f = open('file.py','w')
f.write(repr(rawData))
f.close()
f = open('file1.py','w')
f.write(repr(data))
f.close()
plt.hist(rawData, bins = 60)
plt.show()

#print(myCounter.stop().value)