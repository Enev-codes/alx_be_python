def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 // num2

def main():
    number1 = 10
    number2 = 5
    print("Addition of {} and {} is {}\nSubtraction of {} and {} is {}\nMultiplication of {} and {} is {}".format(number1, number2, add(number1, number2), number1, number2, sub(number1, number2), number1, number2, mul(number1, number2)))


if __name__ == "__main__":
    main()
