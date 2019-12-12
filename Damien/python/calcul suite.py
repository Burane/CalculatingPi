from math import *
from decimal import *

def pi(n):
    getcontext().prec = 323
    p = 0
    r=0
    for k in range(0, n):
        r=Decimal(((-1)**k)/((2*k+1)*3**k))
        p = Decimal(p) + Decimal(((-1)**k)/((2*k+1)*3**k))
    p = Decimal(12).sqrt() * Decimal(p)
    return Decimal(p) ,"nombre décimal sur :", int(log(abs(Decimal(r)),10))
