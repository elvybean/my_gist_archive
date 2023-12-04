def power(base: int, exp: int):
    org_base = base
    for i in range(exp):
        base = base * org_base
    return base

#x_in_litres = 100000
#x_in_ml = x_in_litres * 1000
x_in_litres = 1000
drops = 0
seconds = 0

for i in range(x_in_litres):
    drops = power(2, i)
    x_in_litres = x_in_litres - drops
    seconds += 1
    print("calculating...")

print("it took: ", seconds, "to fill stadium with drops")