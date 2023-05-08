arr1 = list(map(str, input().split()))
n = len(arr1)
split1 = []
split2 = []

for i in range(n):
    ele = str(arr1[i])
    m = len(ele)
    len1 = m / 2
    len2 = m //2
    if len1 > len2:       #cutting the string into two halfes and appending them in diff list
        len2 += 1
        split1.append(ele[0 : len2])  # if len1 is not fixed !
        split2.append(ele[len2 : ])
    else:
        split1.append(ele[0 : len2])
        split2.append(ele[len2 : ])

print(split1)
print(split2)
