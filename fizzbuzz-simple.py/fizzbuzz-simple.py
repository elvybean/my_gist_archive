def main():
    for i in range(0, 100):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"
        else:
            output = i
        print(output)
                
if __name__ == "__main__":
    main()