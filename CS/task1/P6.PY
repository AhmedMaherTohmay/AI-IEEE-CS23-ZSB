boys = input(" ").split(',')
girls = input(" ").split(',')
dict1 = {}

for i in boys:
    x,y = i.split(':')   #getting rid of unwanted chars 
    dict1[x] = int(y)

for i in girls:
    x,y = i.split(':')        #adding them into library
    dict1[x] = int(y)

print(dict1)

