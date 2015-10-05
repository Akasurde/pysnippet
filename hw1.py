#!/usr/bin/env python
# For sqrt function
from math import sqrt

# SOURCE file
srcfile = "data1.txt"


def mean(lst):
    """
    Function to calculate mean of sample data
    """
    sum = 0
    for i in lst:
        sum += int(i)
    return float(sum) / float(len(lst))


def std_dev(lst):
    """
    Function to calculate standard deviation of sample data
    """
    variance = 0
    mn = mean(lst)
    for e in lst:
        variance += (int(e) - mn) ** 2
    variance /= len(lst)

    return sqrt(variance)


def main():
    """
    Main function
    """
    with open(srcfile, 'r') as f:
        # Open file in read mode
        for row in f:
            # For each line in input file
            lst = row.split(",")  # Split output
            if len(lst) > 0:
                lst[-1] = lst[-1].rstrip()

            # Print desired output
            print("Number of element in sample : %d " % (len(lst)))
            print("Mean of %s : %.3f" % (lst, mean(lst)))
            print("Standard deviation of sample : %.3f\n" % (std_dev(lst)))

if __name__ == "__main__":
    # Start of program
    main()
