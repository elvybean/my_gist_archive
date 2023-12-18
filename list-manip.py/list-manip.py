# More list manipulation 
x = [2, 4, 5, 6, 7, 2, 9] # list
print(x)
y = int(input("Enter the number you're looking for: ")) # number searching for

match y in x:
    case True:
        z = x.index(y)
        a = x[x.index(y)]
    case False:
        z = len(x)-1
        a = z[x.index(len(x)-1)]

print(a)
print(z)