"""Sorting Hex Values."""
import csv


def main():
    """The main function of my script."""
    # Read lines from file
    output_list = []
    with open("rainbow.csv", "r") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            output_list.append(row[1])
    for out in sorted(output_list):
        print out

if __name__ == "__main__":
    main()
