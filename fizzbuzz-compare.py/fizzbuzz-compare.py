import time

def simple():
    s_start = time.time()

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

    s_end = time.time()
    return (s_end - s_start)

def _complex():
    c_start = time.time()

    def fizz(i): return i % 3 == 0
    def buzz(i): return i % 5 == 0
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

    c_end = time.time()
    return (c_end - c_start)

def main():
    list = []
    for i in range(10):
        s_time = simple()
        c_time = _complex()
        calc = round((s_time / c_time), 4)
        list.append(calc)

    store = 0
    for elm in list:
        store += elm
    value = store / 10

    print("-----------------")
    print("the complex implementation is on average (factor of 10): ", value," times faster")

if __name__ == "__main__":
    main()