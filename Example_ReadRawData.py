#!/usr/bin/python

from L3GD20 import L3GD20
import time
import numpy
import matplotlib.pylab as plt

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_AxisX_Enabled(False)
s.Set_AxisY_Enabled(False)
s.Set_AxisZ_Enabled(True)
s.Set_DataRateAndBandwidth(95, 12.5)
s.Set_FifoMode_Value("Bypass")
s.CalibrateZ()

plotEnabled = False
if plotEnabled:
    plt.subplot(111)


# Read values loop
starttime = time.time()         # this is our start time
t = 0
prev_z = 0
tmax = 10
T = []
Z = [] 
while t < tmax:
    while s.Get_AxisDataAvailable_Value()[2] == 0:
        time.sleep(0.001)
    t = time.time() - starttime
    z = s.Get_CalOutZ_Value()
    T.append(t)
    Z.append(z)
    if z != prev_z:
        print (z);
        prev_z = z

if plotEnabled:
    plt.plot(T, Z, 'ro')
    plt.show()




