import math


def minimum_maximum(lst):
    """
    returns the maximum and the minimum number in the given list
    """
    return min(lst), max(lst)


def getting_dev_var(lst):
    """
    mean: average of numbers (sum of numbers over their count)
    var : variance of numbers
    dev : standard deviation
    """
    var = 0
    mean = sum(lst) / len(lst)
    for i in range(len(lst)):
        var += (mean - lst[i])**2

    var = var / len(lst)
    dev = math.sqrt(var)
    return var, dev


def getting_q1q2q3IQR(lst):
    """
    sorting list and returning the mid number and the fisrt and the third quartile 
    IQR : The interquartile range 
    """
    lst1 = []
    lst2 = []
    n = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        Q2 = (lst[n] + lst[n - 1]) / 2
        lst1 = lst[:n]
        lst2 = lst[n:]

    else:
        Q2 = lst[n]
        lst1 = lst[:n]
        lst2 = lst[n + 1:]

    n1 = int(len(lst1) / 2)
    n2 = int(len(lst2) / 2)
    if len(lst1) % 2 == 0:
        Q1 = (lst1[n1] + lst1[n1 - 1]) / 2
    else:
        Q1 = lst1[n1]

    if len(lst2) % 2 == 0:
        Q3 = (lst2[n2] + lst2[n2 - 1]) / 2
    else:
        Q3 = lst2[n2]

    IQR = Q3 - Q1
    return Q1, Q2, Q3, IQR


def main():
    while True:
        try:
            lst = list(map(float, input().split()))
            lst.sort()
            break

        except ValueError:      # making sure that a list is entered
            print("Please enter a list of numbers")

        except KeyboardInterrupt:
            exit()

    try:
        minimum, maximum = minimum_maximum(lst)
        q1, q2, q3, IQR = getting_q1q2q3IQR(lst)
        variance, std = getting_dev_var(lst)
        print('min :', minimum)
        print('Q1 : ', q1)
        print('Q2 : ', q2)
        print('Q3 : ', q3)
        print('max :', maximum)
        print('range', lst[-1] - lst[0])
        print('IQR :', IQR)
        print('variance :', round(variance, 3))
        print('standard deviation :', round(std, 3))

    except (ZeroDivisionError, IndexError, ValueError):
        print("You have entered an empty list")
        # to eliminate all the possiple errors
        # zero division error: as the result of dividing empty list on it's lenght
        # index error: due  to zero lenghth will be no median
        # value error: this is due to the empty argument max


main()
