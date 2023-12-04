x = 13
y = 7

match bool( x > 10 + 3 or x > y + 2 or y > x):
    case True:
        print("Yes")
    case False:
        print("No")