import math

#Extended Euclid algorithm
def extEGCD(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while (b > 0):
        q, r = divmod(a, b)
        a, b = b, r
        s0, t0, s1, t1 = s1, t1, s0 - s1 * q, t0 - t1 * q
    return (s0, t0)

#If n and p are coprime, the extended Euclid algorithm returns the multiplicative
#inverses of n and p. This is useful to avoid the modular division.
def inverse(n, p):
    return extEGCD(n, p)[0]

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Values for the Elliptic curve Secp256k1
_a = 0
_b = 7
_q = 115792089237316195423570985008687907853269984665640564039457584007908834671663
_x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
_y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)

_g = Point(_x, _y)

def ecSum(p1, p2):
    if (p1.x == 0 and p1.y == 0): return p2
    if (p2.x == 0 and p2.y == 0): return p1
    if (p1.x == p2.x and p1.y == -p2.y):
        return Point(0, 0)
    if (p1.x == p2.x):
        lam = (3 * (p1.x**2) % _q + _a) * inverse(2 * p1.y, _q) % _q
    else:
        lam = (p2.y - p1.y) * inverse(p2.x - p1.x, _q) % _q
    xr = (lam**2 % _q - p1.x - p2.x) % _q
    yr = (lam * (p1.x - xr) - p1.y) % _q
    return Point(xr, yr)

def ecProd(p, n):
    r = Point(0,0)
    doubleP = p
    while n > 0:
        if n % 2 == 1:
            r = ecSum(r, doubleP)
        n = n >> 1
        doubleP =  ecSum(doubleP, doubleP)
    return r