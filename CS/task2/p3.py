arr1 = list(map(int, input().split()))
maxlst, minlst, temp1, temp2 = [], [], [], []

for i in range(len(arr1)):
    if int(arr1[i]) > 0:
        # appending all of the postive numbers in a list
        maxlst.append(arr1[i])
        temp1.append(arr1[i])

    else:
        minlst.append(arr1[i])      # same for negative
        temp2.append(arr1[i])

if len(maxlst) == 0:
    # making sure that there is numbers that have appended to the list
    maxlst.append(max(minlst))
    # if not append the last two small elements in the other list
    temp2.remove(max(temp2))
    maxlst.append(max(temp2))
elif len(maxlst) == 1:
    # if there is only one number appended append the samallest element in the other element
    maxlst.append(max(minlst))


if len(maxlst) == 0:
    minlst.append(min(maxlst))   # same for min
    temp1.remove(min(temp1))
    minlst.append(min(temp2))
elif len(minlst) == 1:
    minlst.append(min(maxlst))

print(maxlst, sum(maxlst))
print(minlst, sum(minlst))
