"""Mike's script."""
from blake_wrapper import BLAKE
from binascii import hexlify, unhexlify
from random import randint
import csv

char_set = list(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@')
pass_length = 6


def get_random_pass():
    """Get random pass."""
    rand_chars = []
    for index in range(pass_length):
        rand_chars.append(char_set[randint(0, 63)])
    return ''.join(rand_chars)


def reduce(hash_val, column):
    """Reduce function."""
    new_pass = []
    for index in range(pass_length / 2):
        new_pass.append(char_set[
            (int(hash_val[(index*3): (index*3+3)], 16) + column) % 64])
        new_pass.append(char_set[((
            (int(hash_val[(index*3): (index*3+3)], 16) + column) / 64) % 64)])
    return ''.join(new_pass)


def hash(text):
    """Hash function."""
    blake = BLAKE(256).final(text)
    return hexlify(blake)


def create_chain(chain_length, csv_writer):
    """Create chain."""
    passwd = get_random_pass()
    hashed_passwd = hash(passwd)
    for index in range(chain_length):
        new_passwd = reduce(hashed_passwd, index)
        hashed_passwd = hash(new_passwd)
    csv_writer.writerow([passwd, hashed_passwd])


if __name__ == "__main__":
    csv_file = open('rainbow_4k.csv', 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for index in range(10000000):
        create_chain(4000, wr)
