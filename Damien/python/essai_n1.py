from decimal import *
def pi(prec):
    P = prec
    getcontext().prec = int(prec/30)
    C = Decimal(4) / 1
    I = 1
    for i in range(P, 0, -1):
        z = Decimal(4) / (I+2)
        if i%2 == 0:
            z = Decimal.copy_negate(z)
        C += z
        I += 2
    return C

