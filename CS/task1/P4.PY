arr1 = list(map(str, input().split()))
target = int(input())

for i in range(len(arr1)):
    for j in range(i + 1):         # adding every element with each other and comparing them with the target one
        if(int(arr1[j]) + int(arr1[i]) == target):
            print(j,",",i)
