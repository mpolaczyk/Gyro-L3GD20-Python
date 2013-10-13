#!/usr/bin/python

from L3GD20 import L3GD20
import time
import sys, math, pygame

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation (http://codeNtronix.com)")
        pygame.display.set_caption("L3GD20 Gyro Python Library (http://mpolaczyk.pl)")
		
        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-2,0.5,-1),
            Point3D(2,0.5,-1),
            Point3D(2,-0.5,-1),
            Point3D(-2,-0.5,-1),
            Point3D(-2,0.5,1),
            Point3D(2,0.5,1),
            Point3D(2,-0.5,1),
            Point3D(-2,-0.5,1)
        ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

        self.angleX, self.angleY, self.angleZ = 0, 0, 0
        
    def run(self):
        """ Main Loop """
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
        dt = 0.02   # Delta time [s]
        xn = 0        # x(n) [deg]
        yn = 0        # y(n) [deg]
        zn = 0        # z(n) [deg]
        
        while 1==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            time.sleep(dt)
            
            # Read current values
            dxyzn = s.Get_CalOut_Value()
            # Calculate trapezoidal integration
            xn += dxyzn[0] * dt
            yn += dxyzn[1] * dt
            zn += dxyzn[2] * dt
            
            self.screen.fill((0,0,0))
            
            # Will hold transformed vertices.
            t = []
            
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(xn).rotateY(yn).rotateZ(zn)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)

            for f in self.faces:
                pygame.draw.line(self.screen, (255,255,255), (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))
                

            
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
