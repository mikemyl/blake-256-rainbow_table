from blake_wrapper import BLAKE
from binascii import hexlify, unhexlify

if __name__=="__main__":
    blake = BLAKE(256).final(hexlify('Kostas'))
    print(hexlify(blake))

    blake = BLAKE(256).final('Kostas')
    print(hexlify(blake).decode())
