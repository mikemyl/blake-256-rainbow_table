"""Sorting Hex Values."""
import csv
import blake

chain_size = 2500

def hash_lookup(mydict):
    """Lookup Function."""
    lines = [line.rstrip('\n') for line in open('hashes.txt')]
    for line in lines:
        given_hash = line
        print('Checking hash: ' + given_hash)
        hash = given_hash
        passwd = ''
        result = "MpaleC"
        for index in range(chain_size + 1):
            if hash in mydict:
                passwd = find_hash_in_chain(mydict[hash], given_hash)
                if passwd is not None:
                    result = "Success!! Found:  " + passwd
                    break
            passwd = blake.reduce(hash, chain_size - index)
            hash = blake.hash(passwd)
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
    with open("rainbow.csv", "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mydict = dict((rows[1], rows[0]) for rows in spamreader)
        hash_lookup(mydict)


if __name__ == "__main__":
    main()
