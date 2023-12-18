# Shows the correct way to manipulate variables using an external function
def testFunc(var: int):
    var += 5
    var -= 3
    var += 10
    return var / 2

def main():
    var = 90
    
    # incorect
    testFunc(var)
    print(var)
    
    # correct
    var = testFunc(var)
    print(var)

if __name__ == "__main__":
    main()