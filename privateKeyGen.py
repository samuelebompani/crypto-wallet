import os
import struct

def privKey():
    data = os.urandom(32)
    #integers = map(int, data)
    #print(list(integers))
    priv_key = int.from_bytes(data, "big")
    return priv_key