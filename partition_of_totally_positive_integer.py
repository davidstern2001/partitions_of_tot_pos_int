#This is a program for computing the number of partitions of a given totally positive integer in the field Q[sqrt(D)].
import math     #Firstly we import Math Library for some functions used in the program.

#Input:
D = int(input("Input D > 0 for quadratic field Q(sqrt(D)): "))       #This takes the input D for establishing the field Q[sqrt(D)]. The input must be a square-free integer.
a,b = input("Input the integer: 'a + b*omega_D' in the form: 'a b': ").split()
PRINT = input("Do you want to print all the partitions? Input Y/N: ")

#We define the 'omega' coordinate class for integer elements in Q(sqrt(D)):
class Omega:
    omega = "second element of the basis of the integer ring in Q(sqrt(D))"
    def __init__(self,w):
        self.w = w
    
    def __add__(self, other):
        return int(self.w + other.w)
    
    def __mul__(self,other):
        return self.w * other.w
    
    def conj(self):
        if D % 4 == 2 or D % 4 == 3:
            return Omega(-self.w)
        elif D % 4 == 1:
            return Omega(1-self.w)
    
    def norm(self):
        return round(self * self.conj())
    
    def trace(self): 
        return self + self.conj()
        
#We define the omega in two cases. They are essential for defining the ring of integers in Q(sqrt(D)):
if D % 4 == 2 or D % 4 == 3:
    omega = Omega(math.sqrt(D))

elif D % 4 == 1:
    omega = Omega((1+math.sqrt(D))/2)


#Now we define the class of the integers in quadratic field Q(sqrt(D)):
class Quadint:
    alpha = "integer of the form a + b*w_D"

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __eq__(self,other):
        "prints 'True' if 'self' is equal to 'other'"
        return (self.a == other.a) and (self.b == other.b)

    def __repr__(self):
        "prints the representatioin of 'self' - a and b values of the integer"
        return "("+str(self.a)+", "+str(self.b)+")"

    def __gt__(self,other):
        "prints 'True  if 'self' is bigger than 'other' in the lexicographic order"
        if self.a > other.a:
            return True
        elif self.a == other.a and self.b > other.b:
            return True
        else: 
            return False

    def __add__(self,other):
        "returns the sum of two quadratic integers"
        return Quadint(self.a + other.a, self.b + other.b)

    def __sub__(self,other):
        "returns the difference of two quadratic integers"
        return Quadint(self.a - other.a, self.b - other.b)

    def __mul__(self,other):
        "returns the product of two quadratic integers"
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return Quadint(a*c + -omega.norm()*b*d, a*d + b*c + omega.trace()*b*d)
        
    def conj(self):
        "returns the conjugate of the integer"
        a = self.a
        b = self.b
        return Quadint(a+b*omega.trace(),-b)

    def norm(self):
        "returns the norm of the quadratic extension of the integer"
        a = self.a
        b = self.b
        return round((self*self.conj()).a)

    def trace(self):
        "returns the trace of the quadratic extension of the integer"
        a = self.a
        b = self.b
        return round((self + self.conj()).a)

    def is_total_pos(self):
        "prints 'True' if the integer is totally positive"
        total_pos = False
        a = self.a
        b = self.b
        if a + b*omega.w> 0 and a + b*omega.conj().w  > 0:
            total_pos = True
        return total_pos

#We define zero as a quadratic integer:
zero = Quadint(0,0)

#Finally we can define the partition function:
def max(a):
    """returns the maximal irrational coordinate 'b' for rational coordinate 'a'"""
    return math.floor(a/-(omega.conj().w))

def min(a):
    """returns the minimal irrational coordinate 'b' for rational coordinate 'a'"""
    return math.ceil(a/-(omega.w))

def partition(self,other):
    """returns the number of partitions of the integer 'self' with the greatest part 'other'"""
    p = 0       #Number of partitions of the integer

    if self.is_total_pos() == False or other.is_total_pos() == False:      #If 'self' and 'other' are not totally positive, we cannot proceed
        return 0
    other_max = other
    if other_max > self:        #If other > self (in the lexicographical order), we switch them
        other_max = self

    for s in range(other_max.a,0,-1):
        Tmax = max(s)       #Maximal second coordinate we admit
        Tmin = min(s)      #Minimal second coordinate we admit
        if s == other_max.a:
            Tmax = other_max.b
        for t in range(Tmin,Tmax+1):
            beta = Quadint(s,t)     #The candidates for terms in partitions of alpha
            alpha = self - beta     #We declare a new quadratic integer
            if alpha == zero:
                p += 1      #End state
            elif alpha.is_total_pos():        #We check, if the new integer is totally positive 
                p += partition(alpha,beta)      #Then proceed with recursion
            
    return p

def partition_print(self,other):
    def partition_p(self,other,num):
        """prints the partitions of the integer 'self' with the greatest part 'other'"""
        """the algorithm is the same as in the 'partition' function, we however save partition terms"""
        p = 0       #number of partitions of the integer

        if self.is_total_pos() == False and other.is_total_pos() == False:
            return 0
        other_max = other
        if other_max > self:
            other_max = self

        for s in range(other_max.a,0,-1):
            Tmax = max(s)
            Tmin = min(s)
            if s == other_max.a:
                Tmax = other_max.b
            for t in range(Tmin,Tmax+1):
                beta = Quadint(s,t)
                alpha = self - beta

                if alpha == zero:
                    print(num+[beta])       #We save the last partition term
                    p += 1
                elif alpha.is_total_pos():
                    p += partition_p(alpha,beta,num+[beta])     #We call the partition function on alpha and beta with saved partition term
        return p
    p = partition_p(self,other,[])
    return p


alpha = Quadint(int(a), int(b))     #Declaring the input quadratic integer

#Output:
if PRINT == "Y":
    p = partition_print(alpha,alpha)
    print("The total number of partitions of alpha is: " + str(p))
else:
    p = partition(alpha,alpha)
    print("The total number of partitions of alpha is: " + str(p))
