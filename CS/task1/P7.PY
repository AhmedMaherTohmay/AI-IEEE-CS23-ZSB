arr2 = list(map(int, input().split()))
k = int(input())                # number of rotations
m = len(arr2)


if(m + 1 < k):
    c = (k // (m + 1) * (m + 1)) # if the num of rotations is bigger than the given list 
    b = k - c                    # u will have to find the wanted number by making some expressions to get it 
else:                            
    b = k

z = m - b
p = []

for i in range(z , m):           # appending the shifted nums in list
    p.append(arr2[i])

for i in range(0 , z):            # then appending the shifted list in same list after shifted nums
    p.append(arr2[i])
print(p)