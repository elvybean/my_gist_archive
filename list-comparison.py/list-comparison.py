base = [True, False, True, False]

test1 = [True, True, True, False]
test2 = [True, True, True, True]
test3 = [True, False, True, False]

listOfLists = [test1, test2, test3]

for item in listOfLists:
    if item == base:
        print("pass")
    else:
        print("fail")