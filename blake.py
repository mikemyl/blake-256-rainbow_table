from blake_wrapper import BLAKE
from binascii import hexlify, unhexlify
from random import randint
import csv

char_set = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@')
pass_length = 6

def get_random_pass():
    rand_chars = []
    for index in range(pass_length):
        rand_chars.append(char_set[randint(0, 63)])
    return ''.join(rand_chars)

def reduce(hash_val):
    new_pass = []
    print(hash_val)
    for index in range(pass_length):
        new_pass.append(char_set[int(hash_val[(index*2) : (index*2+2)], 16) % 64])
    return ''.join(new_pass)

def hash(text):
    blake = BLAKE(256).final(text)
    return hexlify(blake)

if __name__=="__main__":
    csv_file = open('rainbow.csv', 'wb')
    #wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    #wr.writerow(['', hexlify(blake)])
    for index in range(10):
        passwd = get_random_pass()
        hashed_passwd = hash(passwd)
        reduced_hash = reduce(hashed_passwd)
        print(passwd + '  ->   ' + hashed_passwd + '   ->  ' + reduced_hash)
