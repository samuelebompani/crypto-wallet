import os
import struct

data = os.urandom(32)
#integers = map(int, data)
#print(list(integers))
priv_key = int.from_bytes(data, "big")
print(priv_key)