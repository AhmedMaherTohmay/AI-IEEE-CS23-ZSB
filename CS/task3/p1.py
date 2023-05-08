import math


def getting_mean(lst):
    """
    mean: average of numbers (sum of numbers over their count)
    """
    mean = sum(lst) / len(lst)
    return mean


def getting_median(lst):
    """
    sorting list and returning the mid number 
    """
    lst = sorted(lst)
    n = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        return (lst[n] + lst[n - 1]) / 2
    else:
        return lst[n]


def getting_mode(lst):

    # s = set(lst)

    # if len(s) == len(lst):
    # return "there is no mode"

    # ss = list(s)
    # freq = [lst.count(i) for i in ss]

    # maxindex = freq.index((max(freq)))
    # return ss[maxindex]
    """getting the most repaeated number
    """

    dic = {}
    repetitions = []
    mode = []

    for i in list(set(lst)):
        dic[i] = lst.count(i)
        repetitions.append(lst.count(i))

    temp = set(repetitions)

    if len(temp) < 2:
        return "No mode"
    else:
        for i in list(dic.keys()):
            if dic[i] == max(temp):
                mode.append(i)

    return mode


def main():
    while True:
        try:
            lst = list(map(float, input().split()))
            break

        except ValueError:      # making sure that a list is entered
            print("Please enter a list of numbers")

        except KeyboardInterrupt:
            exit()

    try:
        print("Mean :", "%.2f" % (getting_mean(lst)))
        print("Median :", getting_median(lst))
        print("Mode :", (getting_mode(lst)))

    except (ZeroDivisionError, IndexError, ValueError):
        print("You have entered an empty list")
        # to eliminate all the possiple errors
        # zero division error: as the result of dividing empty list on it's lenght
        # index error: due  to zero lenghth will be no median
        # value error: this is due to the empty argument max


main()
