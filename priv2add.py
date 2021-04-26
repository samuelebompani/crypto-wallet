# An elliptic curve is defined by the equation y^2 = x^3 + a*x +b
# ecc.py should give a valid implementation of elliptic curves

import ecc
import hashlib as h
import base58
import privateKeyGen as priv

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

#Secp256k1 equation is y^2 mod q = x^3 + 0*x + 7 mod q (a = 0, b = 7)
#G is the base point for the product operation
a = 0
b = 7
q = 115792089237316195423570985008687907853269984665640564039457584007908834671663
x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)

g = Point(x, y)
#e = ecc.EC(0,7,q)

#Input: a valid private key
#Output: a tuple in the form (privateKey, publicKey, P2PKH address)
def getAddress(privateKey):
    #r = e.mul(g, privateKey)
    r = ecc.ecProd(g, privateKey)
    p1 = hex(r.x)[2:]
    p2 = hex(r.y)[2:]
    while len(p1) < 64: 
        p1 = "0"+p1
    while len(p2) < 64: 
        p2 = "0"+p2
    #public key = "04" | r.x | r.y
    publicKey = "04"+p1+p2

    tmp = publicKey
    if(len(tmp)%2!=0):
        tmp="0"+tmp
    #Double hash with SHA-256 and RIPEMD-160
    tmp=h.sha256(bytes.fromhex(tmp)).digest()
    x=h.new('ripemd160')
    x.update(tmp)
    tmp=x.hexdigest()
    #00 is a Bitcoin network prefix
    tmp="00"+tmp
    #Double hash with SHA-256
    tmpnew=h.sha256(bytes.fromhex(tmp)).digest()
    tmpnew=h.sha256(tmpnew).hexdigest()
    tmp=tmp+tmpnew[0:8]
    #P2PKH address:
    p2pkh = "1"+base58.encode(bytes.fromhex(tmp))
    return (privateKey, publicKey, p2pkh)