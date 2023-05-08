dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}

x = 0
n = list(dict1.keys())[0]

for key in dict1:
    temp = max(dict1[key]) - min(dict1[key])   # getting the diff then comparing it with others
    print(dict1[key])
    print(temp)
    if(temp > x):
        x = temp
        n = key


print(n)