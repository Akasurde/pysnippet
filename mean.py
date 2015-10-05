from math import sqrt

def mean(lst):
    """calculates mean"""
    return sum(lst) / len(lst)

def stddev(lst):
    """returns the standard deviation of lst"""
    variance = 0
    mn = mean(lst)
    for e in lst:
        variance += (e-mn)**2
    variance /= len(lst)

    return sqrt(variance)


def main():
    a = [1, 2, 3, 19, 12, 123]
    print(mean(a))
    print(stddev(a))

if __name__ == "__main__":
    main()
