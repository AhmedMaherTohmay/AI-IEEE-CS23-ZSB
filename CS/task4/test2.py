"""lst = list(map(float, input().split()))

lst1 = []
lst2 = []
lst = sorted(lst)
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

print(Q1, Q2, Q3, IQR)"""


from math import sqrt
# import statistics


def get_median(l): n = len(l); return round((l[n//2] + l[-(n//2+1)])/2, 2)
def split_lst(l, n): return (l[:(n+1)//2], l[n//2:])


def get_all_q(lst):
    first_half, second_half = split_lst(lst, len(lst))
    q1 = get_median(first_half)
    q2 = get_median(lst)
    q3 = get_median(second_half)
    return q1, q2, q3


def get_variance(data):
    mean = sum(data) / len(data)
    return sum([(x-mean)**2 for x in data]) / len(data)


def solve():
    lst = sorted([int(i) for i in input().split()])

    datavariance = get_variance(lst)
    standard_deviation = sqrt(datavariance)

    q1, q2, q3 = get_all_q(lst)
    print('min :', lst[0])
    print('Q1 : ', q1)
    print('Q2 : ', q2)
    print('Q3 : ', q3)
    print('max :', lst[-1])
    print('range', lst[-1]-lst[0])
    print('IQR :', q3-q1)
    print('variance :', round(datavariance, 3))
    print('standard deviation :', round(standard_deviation, 3))


if __name__ == "__main__":
    solve()


'''
https://calculator-online.net/quartile-calculator/
9 8 7 10 9 1 4
12 32 12 33 4 21 13 34
min : 4
Q1 :  12.0
Q2 :  17.0
Q3 :  32.5
max : 34
'''
