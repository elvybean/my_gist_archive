#This code snippet deletes all items except a SPECIFIED item
list = ["Q", "W", "E", "R", "T", "Y"]
ideal_num = "Q"
print("orginal list: ", list)

while len(list) != 1:
    for item in list:
        match item == ideal_num:
            case False:
                del list[list.index(item)]

print("list after logic: ", list)