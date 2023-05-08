
import math


def quartails(lst):
    q = []
    lst.sort()
    firsthalf = len(lst)//2
    if len(lst) % 2 == 0:
        if firsthalf % 2 == 0:
            Q1 = (lst[firsthalf//2]+lst[firsthalf//2 - 1])/2
            q.append((Q1))
        else:
            Q1 = lst[firsthalf // 2]
            q.append(Q1)
        median1 = lst[len(lst) // 2]
        median2 = lst[len(lst) // 2 - 1]
        median = (median1 + median2)/2
        q.append(median)
        if firsthalf % 2 == 0:
            Q3 = (lst[(firsthalf//2)+firsthalf] +
                  lst[(firsthalf//2 - 1)+firsthalf])/2
            q.append(Q3)
        else:
            Q3 = lst[(firsthalf//2)+firsthalf]
            q.append(Q3)
    else:
        if firsthalf % 2 == 0:
            Q1 = (lst[firsthalf//2]+lst[firsthalf//2 - 1])/2
            q.append((Q1))
        else:
            Q1 = lst[firsthalf // 2]
            q.append(Q1)
        median = lst[len(lst) // 2]
        q.append(median)
        if firsthalf % 2 == 0:
            Q3 = (lst[(firsthalf//2)+firsthalf] +
                  lst[(firsthalf//2 + 1)+firsthalf])/2
            q.append(Q3)
        else:
            Q3 = lst[(firsthalf//2)+firsthalf+1]
            q.append(Q3)
    return q


def IQR(a, b):
    c = a-b
    return c


def variance(lst):
    mean = sum(lst)/len(lst)
    summ = 0
    for i in range(len(lst)):
        summ = summ+(lst[i]-mean)**2
    var = summ/len(lst)
    return var


def stdev(lst):
    var = variance(lst)
    std_dev = math.sqrt(var)
    return std_dev


try:
    lst = []
    lst = list(map(int, input().split()))
    q = quartails(lst)
    print("min : ", min(lst))
    print("Q1 : ", q[0])
    print("Q2 : ", q[1])
    print("Q3 : ", q[2])
    print("max : ", max(lst))
    print("Range : ", max(lst)-min(lst))
    print("IQR : ", IQR(q[2], q[0]))
    print("variance : ", variance(lst))
    print("standard deviation : ", stdev(lst))
except ValueError:
    print("invalid input")
except:
    print("there is an error")
