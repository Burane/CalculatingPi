from decimal import *
from math import *

def essai(n):
    getcontext().prec = n
    return Decimal(sqrt(2))
