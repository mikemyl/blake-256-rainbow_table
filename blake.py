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
    for index in range(pass_length):
        new_pass.append(char_set[int(hash_val[(index*2) : (index*2+2)], 16) % 64])
    return ''.join(new_pass)

def hash(text):
    blake = BLAKE(256).final(text)
    return hexlify(blake)

def create_chain(chain_length, csv_writer):
    passwd = get_random_pass()
    hashed_passwd = hash(passwd)
    for index in range(chain_length):
        new_passwd = reduce(hashed_passwd)
        hashed_passwd = hash(new_passwd)
    csv_writer.writerow([passwd, hashed_passwd])


if __name__=="__main__":
    csv_file = open('rainbow.csv', 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for index in range(10):
        create_chain(10, wr)
