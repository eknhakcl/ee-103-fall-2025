from math import sqrt , pi
class Coord():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def disstance(self,other):
        xvalue = (self.x - other.x)**2
        yvalue = (self.y - other.y)**2
        return sqrt(xvalue + yvalue)
    

class Circle():
    def __init__(self, center , radius):
        if type(center) == Coord and type(radius) == int :
            self.center = center
            self.radius = radius
        else: 
            raise ValueError

    def area(self):
        return round(pi*(self.radius**2),2)
    
    def is_incircle(self,point):
        if self.center.disstance(point)< self.radius :
            return "Point is on the circle."
        else :
            return "Point is not on the circle."
    
