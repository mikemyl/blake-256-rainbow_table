"""Sorting Hex Values."""
import csv
import sys
import blake

chain_size = 4000
rainbow_file = 'rainbow.csv'
hashes_file = 'hashes.txt'

def hash_lookup(mydict):
    """Lookup Function."""
    while True:
        given_hash = raw_input("Give the hash: \n")
        hash = given_hash
        passwd = ''
        result = "Could not revert hash: " + given_hash
        if hash in mydict:
            passwd = find_hash_in_chain(mydict[hash], given_hash)
            if passwd is not None:
                result = "Found password: " + passwd
            print result
            continue
        for index in range(chain_size):
            for i in range(index, -1, -1):
                passwd = blake.reduce(hash, chain_size - i - 1)
                hash = blake.hash(passwd)
            if hash in mydict:
                passwd = find_hash_in_chain(mydict[hash], given_hash)
                if passwd is not None:
                    result = "Found password: " + passwd
                    break
            hash = given_hash
        print result

def find_hash_in_chain(passwd, given_hash):
    for index in range(chain_size + 1):
        new_hash = blake.hash(passwd)
        if new_hash == given_hash:
            return passwd
        passwd = blake.reduce(new_hash, index)
    return None


def main():
    """The main function of my script."""
    # Read lines from file
    with open(rainbow_file, "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mydict = dict((rows[1], rows[0]) for rows in spamreader)
        hash_lookup(mydict)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        rainbow_file = sys.argv[1]
    if len(sys.argv) == 3:
        rainbow_file = sys.argv[1]
        chain_size = int(sys.argv[2])
    main()
