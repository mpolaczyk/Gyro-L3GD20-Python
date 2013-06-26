#!/usr/bin/python

from L3GD20 import L3GD20

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(False)
s.Set_AxisZ_Enabled(False)

# Print current configuration
for a, b in s.ReturnConfiguration():
    print(str(a) + ': ' + str(b))


