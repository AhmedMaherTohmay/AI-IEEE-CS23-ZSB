def sort_list():
    """
    arr1 : reciveing input 
    iterating in a loop to sort the list
    returning the sorted list
    Note u can use sort method to do the samething
    """
    arr1 = list(map(int, input().split()))
    for i in range(len(arr1)):
        for j in range(i + 1, len(arr1)):

            if arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]
    return arr1


def appear(arr2):
    """
    function to know the first and lasst appearance of a given number
    target: the wanted numer 
    apearance: a list to get all the appearances of the number then returning the first and last appearance of the number
    """
    appearance = []
    target = int(input())
    for i in range(len(arr2)):
        if int(arr2[i]) == target:
            appearance.append(i)
    return appearance[0], appearance[len(appearance) - 1]


lst = sort_list()
x, c = appear(lst)

print(x, c)
