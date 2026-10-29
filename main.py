import math

G = 9.81
framerate = 60


class system:
    def __init__(self, objects,surfaces):
        objects = self.objects

class object:
    def __init__(self, mass, actingforces,direction,acceleration):
        mass = self.mass
        actingforces = []
        gravity = force((mass * G),-90)
        actingforces.append(gravity)

        ax = 0
        ay = 0

        for i in range(0,len(actingforces)):
            ax += (actingforces[i].magnitude) * math.cos(math.radians((actingforces[i])))
            ay += (actingforces[i].magnitude) * math.sin(math.radians((actingforces[i])))
            ax = ax/mass
            ay = ay/mass
        acceleration = math.sqrt(ax**2 + ay**2)
        direction = math.degrees(math.atan(ay/ax))

class surface:
    def __init__(type):

        
class force:
    def __init__(self,magnitude, direction):    
        magnitude = self.magnitude
        direction = self.direction

