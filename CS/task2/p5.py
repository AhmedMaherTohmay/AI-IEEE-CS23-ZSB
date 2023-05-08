from p4 import users


def write(filename, users):
    with open("filtered.txt", "w") as f:
        for i in users.keys():
            arr1 = "{} {} - {}\n".format(i,
                                         users[i]['name'], users[i]['birthyear'])

            f.write(arr1)


write("filtered.txt", users)
