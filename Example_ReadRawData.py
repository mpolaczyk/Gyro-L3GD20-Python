#!/usr/bin/python

from L3GD20 import L3GD20
import time

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

    
# Read values loop
while True:
    time.sleep(1)
    xeps = s.Get_OutX_Value()
    yeps = s.Get_OutY_Value()
    zeps = s.Get_OutZ_Value()
    print (xeps, yeps, zeps)



