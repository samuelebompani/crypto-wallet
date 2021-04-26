#Base58 is similar to Base64, but with a diferent charset:
b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def encode(b):
    rap = 0
    for counter, i in enumerate(b[::-1]):
        rap += i*(2**(counter*8))
    dividend = rap
    quotient = rap
    mods = list()
    while(quotient != 0):
        quotient, reminder = divmod(dividend, 58)
        mods.append(b58chars[int(reminder)])
        dividend = quotient
    return ("".join(mods[::-1]))