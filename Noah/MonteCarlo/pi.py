from decimal import Decimal

def setup() :
    
    P = 10000000
    C = Decimal(4) / 1
    I = 1
    for i in range(P,0,-1):
        z = Decimal(4) / (I+2)
        if i%2 == 0:
            z = Decimal.copy_negate(z)
        C = C + z
        I = I + 2
    print(C)    
        
def draw() :
     P = 10000000
    C = Decimal(4) / 1
    I = 1
    for i in range(P,0,-1):
        z = Decimal(4) / (I+2)
        if i%2 == 0:
            z = Decimal.copy_negate(z)
        C = C + z
        I = I + 2
    print(C)
