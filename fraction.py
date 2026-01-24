class SimpleFraction ():
    def __init__ ( self , n , d):
        self.num = n
        self.denom = d 
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else :
            return str(self.num) + "/" + str(self.denom)
    
    def multi(self, oth):
        if type(oth)== SimpleFraction:
            top = self.num * oth.num
            bottom = self.denom * oth.denom
            return round(top/bottom,3)
        else:
            raise TypeError
    
    def plus (self,oth):
        if type(oth) == SimpleFraction:
            top = self.num*oth.denom + self.denom*oth.num
            bottom = self.denom * oth.denom
            return round(top/ bottom,3)
        else:
            raise TypeError
    
    def get_inverse (self):
        return self.denom/self.num
    
    def invert(self):
        new_num = self.denom
        new_denom = self.num
        self.num = new_num
        self.denom = new_denom
        
