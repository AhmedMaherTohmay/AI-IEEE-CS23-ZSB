users = dict()
temp1 = 1            # old
temp2 = 1            # highscore
lst = []             # to save the scores in

with open('grades.txt') as f:       # importing the data from the file and saving it in vars
    f.readline()
    for line in f:
        arr1 = line.split()
        try:
            Id = int(arr1[0])
            Name = arr1[1]
            Score = int(arr1[2])
            Birth = int(arr1[4])
            Gender = arr1[6]

            if Gender == 'm':
                Gender = "Male"
            else:
                Gender = "Female"

            users[Id] = {'name': Name,         # creating the dict from the data collected
                         'score': Score,
                         'birthyear': Birth,
                         'gender': Gender
                         }
            lst.append(users[Id]['score'])

        except:
            continue

        # copmaring to get the oldest member ID
        if (users[Id]['birthyear'] < users[temp1]['birthyear']):
            temp1 = Id
        # comparing to get the highest score
        if (users[Id]['score'] > users[temp2]['score']):
            temp2 = Id

avg = 0
for i in range(len(lst)):
    avg += int(lst[i]) / len(lst)

if __name__ == "__main__":
    print("The ID of the oldest user is: {}".format(temp1))
    print("The average score is: {}".format(avg))
    print(
        "The sex of the user with the highest Score is: {}".format(users[temp2]['gender']))
