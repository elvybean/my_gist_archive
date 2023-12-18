# Calculate what percent of a given number (x) is of a larger number (y) and works out the percentage (z)
print("---- What percentage of y is x calculator ---- \n\n")

x = int(input("x which is the number given "))
y = int(input("y which is the larger number that is 100% "))

z = x/(y/100)

print(x, " is ", z, "%"" of", y)