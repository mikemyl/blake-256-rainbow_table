"""Sorting Hex Values."""
import csv


def hash_lookup(mydict):
    """Lookup Function."""
    while True:    # infinite loop
        input_u = raw_input("\n\Give the hash: ")
        if input_u in mydict:
            print("Success!!")
            print mydict[input_u]
        else:
            print("Not Found")


def main():
    """The main function of my script."""
    # Read lines from file
    with open("rainbow.csv", "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mydict = dict((rows[1], rows[0]) for rows in spamreader)
        hash_lookup(mydict)

if __name__ == "__main__":
    main()
