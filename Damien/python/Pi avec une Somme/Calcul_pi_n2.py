from math import *
from decimal import *
from time import time


def pi(n):
    getcontext().prec = n # à changer si vous ne voulez pas que le programme soit trop gourmand
    #start = time()	#permet à calculer la vitesse (en s) à la quelle le programme se fait
    p = Decimal(0)
    for k in range(0, n):
        r = ( Decimal(-1)**k ) / ( Decimal(2*k+1) * Decimal(3**k) )
        p = Decimal(p) + Decimal( r )
    p = Decimal(12).sqrt() * Decimal(p)
    #end = time()
    #print("fini en {0} s".format(end - start))
    return Decimal(p)
