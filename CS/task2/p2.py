arr1 = list(map(int, input().split()))
even = list(filter(lambda x: (x % 2 == 0), arr1))
print(len(even))
