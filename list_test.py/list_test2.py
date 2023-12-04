#Whereas this code snippet deletes all items in a list except the LAST item
list = ["Q", "W", "E", "R", "T", "Y"]
print("orginal list: ", list)

del list[:len(list)-1]

print("list after logic: ", list)