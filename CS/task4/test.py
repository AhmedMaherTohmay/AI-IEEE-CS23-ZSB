"""import math
# All errors are handled in the main function


def minimum_maximum(lst: list):
  
    :param lst:
    :return: maximum and minimum
 
    return max(lst), min(lst)


def q1_q2_q3_IQR(lst: list):
   
    :param lst:
    :return: 1st, 2nd, and 3rd Quartile + InterQuartile Range
    Disclaimer: Could be done using direct one-line equation e.g. q3 = (3 * (N + 1) / 4)
 

    lst = sorted(lst)
    x = int(len(lst) / 2)
    # Slicing the list to get 1st Quartile and 3rd Quartile
    # Case of even number of elements
    if len(lst) % 2 == 0:
        q2 = (lst[x] + lst[x - 1]) / 2
        lst_q1 = lst[:x+1]
        lst_q3 = lst[x:]

        # Handle special case of only 2 elements
        if len(lst) == 2:
            q1 = lst[0]
            q3 = lst[1]
        else:
            q1 = (lst_q1[int(len(lst_q1) / 2)] +
                  lst_q1[int(len(lst_q1) / 2) - 1]) / 2
            q3 = (lst_q3[int(len(lst_q3) / 2)] +
                  lst_q3[int(len(lst_q3) / 2) - 1]) / 2

    # Case of odd number of elements
    else:
        q2 = lst[x]
        lst_q1 = lst[:x]
        lst_q3 = lst[x+1:]

        # Handle special case of one element
        if len(lst_q1) == 0:
            q1, q2, q3 = lst[0], lst[0], lst[0]
        else:
            q1 = lst_q1[int(len(lst_q1) / 2)]
            q3 = lst_q3[int(len(lst_q3) / 2)]

    return q1, q2, q3, q3 - q1


def variance_STDN(lst: list):
    
    :param lst:
    :return: variance and standard deviation for a population NOT sample

    x = len(lst)
    mean = sum(lst) / x

    for i in range(len(lst)):
        lst[i] = round((lst[i] - mean) ** 2, 3)

    variance = sum(lst) / x

    return variance, math.sqrt(variance)


if __name__ == '__main__':
    # Handling Error of wrong Input
    while True:
        try:
            lst_input = list(map(float, input().split()))
            break
        except ValueError:
            print("Please enter a list of numbers")

    # try:
    #     Flag = int(input("Please type 1 if list represent a sample and 2 if it represent a population"))
    # except ValueError:
    #     print("ENTER 1 or 2!!!!!!!!")

    try:
        M, m = minimum_maximum(lst_input)
        Q1, Q2, Q3, Iqr = q1_q2_q3_IQR(lst_input)
        var, stdn = variance_STDN(lst_input)

        print("min:", m)
        print("Q1:", Q1)
        print("Q2:", Q2)
        print("Q3:", Q3)
        print("max:", M)
        print("range:", M - m)
        print("IQR:", Iqr)
        print("Variance", "%.4f" % var)
        print("Standard Deviation:", "%.3f" % stdn)

    except (ZeroDivisionError, IndexError, ValueError):
        print("Empty List")"""


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:31:25 2023

@author: Rami
"""


def Q(nslst: list):
    """


    Parameters
    ----------
    nslst : not sorted list
        the list from which we will get the 3 quartiles.

    Returns
    -------
    Q : list
        List containing Q1,Q2,Q3.

    """
    Q = []
    n = len(nslst)
    lst = nslst.copy()
    lst.sort()
    half = n//2
    quartile1Int = (n)//4
    quartile2Int = 3*(n)//4

    if (n % 2 == 0 and n > 0):
        Q.append((lst[quartile1Int] + lst[quartile1Int-1])/2)
        Q.append((lst[half] + lst[half - 1])/2)
        Q.append((lst[quartile2Int] + lst[quartile2Int-1])/2)
    elif (n % 2 != 0):
        Q1 = int(lst[quartile1Int])
        Q2 = int(lst[half])
        Q3 = int(lst[quartile2Int])
        Q.append(Q1)
        Q.append(Q2)
        Q.append(Q3)
    return Q


def fiveNumberSummary(nslst: list, Q):
    """


    Parameters
    ----------
    nslst : not sorted list
        the list from which we will get the minimum , 3 quartiles and maximum.
    Q : function
        function that returns the 3 quartiles.

    Prints
    -------
    The 5 number Summary

    """
    minimum = min(nslst)
    maximum = max(nslst)
    Q = Q(nslst)
    Q1 = Q[0]
    Q2 = Q[1]
    Q3 = Q[2]

    print("min: {}\nQ1: {}\nQ2: {}\nQ3: {}\nmax: {}".format(
        minimum, Q1, Q2, Q3, maximum))
    numberSummary = {'min': minimum, 'Q1': Q1,
                     'Q2': Q2, 'Q3': Q3, 'max': maximum}
    return numberSummary


def spread(numberSummary):
    """


    Parameters
    ----------
    numberSummary : dictionary
        dict that has the 5 number summary.

    Prints
    -------
    the Range and the IQR

    """
    listRange = numberSummary['max'] - numberSummary['min']
    IQR = numberSummary['Q3'] - numberSummary['Q1']
    print("range: {}\nIQR: {}".format(listRange, IQR))


def variance(nslst):
    """
    Note : assumed input is *population*

    Parameters
    ----------
    nslst : list
        not sorted list .

    Prints
    -------
    The variance and standard deviation (population).

    """
    mean = sum(nslst)/len(nslst)
    variance = 0
    for i in nslst:
        variance += (i-mean)**2
    variance = variance/(len(nslst))
    standardDeviation = variance ** 0.5
    print("Variance:%0.3f" % (variance))
    print("Standard deviation:%0.3f" % (standardDeviation))


print("Input:")
lst = []
while True:
    try:
        splitted = input().split()
        lst = [float(x) for x in splitted]
        break
    except ValueError:
        print("please enter only numbers")
    except KeyboardInterrupt:
        print("Ended")
        break
if (lst):
    print("\nOutput:")
    numberSummary = fiveNumberSummary(lst, Q)
    spread(numberSummary)
    variance(lst)
