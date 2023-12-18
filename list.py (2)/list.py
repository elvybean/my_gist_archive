# Select the last element of a list or a specified element 
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("list: ",_list)
x = input("Enter last or choice: ")

match x:
    case "choice":
        y = int(input("Enter yoour choosen number: "))
        bestFit = _list[_list.index(y)]
    case "last":
        bestFit = _list[_list.index(len(_list))]
    case other:
        print("ERROR.")

print(bestFit)