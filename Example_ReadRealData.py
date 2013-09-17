#!/usr/bin/python

from L3GD20 import L3GD20

import time

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)

# Print current configuration
s.Init()
s.Calibrate()

# Calculate angle
dt = 0.02
x = 0
y = 0
z = 0
while 1==1:
	time.sleep(dt)
	dxyz = s.Get_CalOut_Value()
	x += dxyz[0]*dt;
	y += dxyz[1]*dt;
	z += dxyz[2]*dt;
	print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))


