import base58 as b58
import wecc as ecc1
import ecc
import priv2add

############################################

assert(b58.encode('Cat'.encode()) == 'PdgX')
assert(b58.encode('12345'.encode()) == '6YvUFcg')
assert(b58.encode('12345678900987654321'.encode()) == 'gkdhQDvLi23xxgmYXRkKeWzMYN4')
print("base58 test passed")

############################################

a = 0
b = 7
q = 115792089237316195423570985008687907853269984665640564039457584007908834671663
x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
ec1 = ecc1.EC(a, b, q)
p = ecc.Point(x, y)

for i in range(1, 10):
    assert(ecc.ecProd(p, i).x==ec1.mul(p, i).x)

print("ecc test passed")

############################################

privkeys = [
    "B86FB533ACBF5731910F4D882E8E960760DDC6424DF68434E1A1501B5ACD29DF",
    "ECD9CF4ADF36AA4DA36ADE586524C305310F196046495E1281EE0AA8D1F0D3FB",
    "6C68D94F9AB902A7F846905A6904034109534CBFAEB5169849884F5DC0FE8CCA",
    "30A1B7FDE4F0C309095C26810FEA4DA4024CE43E64E5A5AD2725C520A7B54D2C",
    "19ADEC76D3AD3318D5D2E872D0A7064492D7992D8F3ED399BA9DA359F0B0EF54"
]

addresses = [
    "18E3GBSAJHrqQVoq1rSyUzFoJscM6CSUCe",
    "1CdAS6XNZMNLbUPA8gVjqSJkkGWKr2NBrN",
    "1Acf9yfhbSJ4Bm1X3xrvmxVbWxmkJ7Y1Ze",
    "15PnsuE96aSvTdahJEymwuJfYtTnAa4qMc",
    "14odkHo3AMofRG73xaLBMvkBAQHPWzcS5v"
]

for c, i in enumerate(privkeys):
    assert(priv2add.getAddress(int(i, 16))[2] == addresses[c])

print("priv2add test passed")