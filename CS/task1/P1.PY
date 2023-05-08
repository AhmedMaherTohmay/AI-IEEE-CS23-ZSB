arr1 = list(map(int, input().split()))
arr1.sort()
n = len(arr1)                      # sorting and displaying the wanted numbers
print(arr1[n - 2])
print(arr1[1])
