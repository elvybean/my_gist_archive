def main():
    fizz = lambda i: i % 3 == 0
    buzz = lambda i: i % 5 == 0

    for i in range(0, 100):
        i += 1
        match [fizz(i), buzz(i)]:
            case [True, True]:
                output = "FizzBuzz"
            case [True, False]:
                output = "Fizz"
            case [False, True]:
                output = "Buzz"
            case [False, False]:
                output = i
        print(output)
                
if __name__ == "__main__":
    main()