"""Sorting Hex Values."""
import csv
import operator


def main():
    """The main function of my script."""
    # Read lines from file
    output_list = []
    with open("rainbow.csv", "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mydict = dict((rows[0], rows[1]) for rows in spamreader)


if __name__ == "__main__":
    main()
