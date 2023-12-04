def func(x):
    match x == 10:
        case True:
            return print("x is 10")


def main():
    x = 10
    func(x)
    x = input("Type: ")
    func(x)


if __name__ == "__main__":
    main()