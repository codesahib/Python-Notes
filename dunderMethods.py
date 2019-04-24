<<<<<<< HEAD
class Vector:
    def __init__(self,*coeffs):
        self.coeffs=coeffs 
    def __repr__(self):
        return 'Vector(*{!r})'.format(self.coeffs)
    def __add__(self,other):
        return Vector(*(x+y for x,y in zip(self.coeffs,other.coeffs))) #Vector object is returned
    def __len__(self):
         return len(self.coeffs)
    def __call__(self,*coeffs):
          self.coeffs=coeffs 
P1=Vector(1,2,3) 
P2=Vector(2,2,4) 
P3=P1+P2

=======
class Vector:
    def __init__(self,*coeffs):
        self.coeffs=coeffs 
    def __repr__(self):
        return 'Vector(*{!r})'.format(self.coeffs)
    def __add__(self,other):
        return Vector(*(x+y for x,y in zip(self.coeffs,other.coeffs))) #Vector object is returned
    def __len__(self):
         return len(self.coeffs)
    def __call__(self,*coeffs):
          self.coeffs=coeffs 
P1=Vector(1,2,3) 
P2=Vector(2,2,4) 
P3=P1+P2

>>>>>>> d9174b9fcd5ffba207cc2e560d720eb917727710
