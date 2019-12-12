from math import *
from decimal import *
from time import time


def pi(n):
    precision = 20000
    getcontext().prec = precision
    start = time()
    p = Decimal(0)
    for k in range(0, n):
        r = ( Decimal(-1)**k ) / ( Decimal(2*k+1) * Decimal(3**k) )
        p = Decimal(p) + Decimal( r )
        
    
    p = Decimal(12).sqrt() * Decimal(p)

    with open("pi-{0}-{1}.txt".format(precision,n), "w") as f:
        f.write(str(Decimal(p))[2:])
    end = time()
    print("fini en {0} s".format(end - start))

    return Decimal(p)
