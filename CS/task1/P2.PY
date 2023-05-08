arr1 = list(map(int, input().split()))

if arr1 == arr1[::-1]:              # checking if the reverse matrix is same as the original one
    print("Symmetric")
else:
    print("Not Symmetric")


