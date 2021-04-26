# An elliptic curve is defined by the equation y^2 = x^3 + a*x +b
# The equation of Secp256k1 is y^2 = x^3 + 7 (a = 0, b = 7)
# ecc.py should give a valid implementation of elliptic curves
# base58.py is an implementation of base58

import ecc
import hashlib as h
import base58
import privateKeyGen as priv

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

a = 0
b = 7
q = 115792089237316195423570985008687907853269984665640564039457584007908834671663
x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
g = (x, y)

p = Point(x, y)
e = ecc.EC(0,7,q)

def getAddress(privateKey):
    r = e.mul(p, privateKey)
    p1 = hex(r.x)
    p2 = hex(r.y)
    print("Private key: "+str(hex(privateKey)[2:]))
    print("Public key: 04"+p1[2:]+p2[2:])

    ris = "04"+p1[2:]+p2[2:]
    if(len(ris)%2!=0):
        ris="0"+ris
    ris=h.sha256(bytes.fromhex(ris)).digest()
    x=h.new('ripemd160')
    x.update(ris)
    ris=x.hexdigest()
    ris="00"+ris
    risnew=h.sha256(bytes.fromhex(ris)).digest()
    risnew=h.sha256(risnew).hexdigest()
    ris=ris+risnew[0:8]
    return "1"+base58.encode(bytes.fromhex(ris))