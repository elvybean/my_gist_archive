# Experimenting with match-case statements (python 3.10) 
value = input("Enter a value for 'value': ")
value2 = input("Enter a value for 'value2': ")

match value > value2:
    case True:
        print("'value' is greater than 'value2'")
    case False:
        print("'value' is NOT greater than 'value2'")