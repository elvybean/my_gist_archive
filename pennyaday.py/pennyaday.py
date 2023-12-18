# calculates how much money would be earned 
# if you saved a penny more than the day before
# Penny a day challange 

x = 0
for i in range (0,365):
    x = x + (i + 1)
print("£",x/100)