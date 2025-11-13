def predict():
    age = int(input("How old are you? "))
    f_age = age + (2050 - 2023)
    print("In 2050, you will be {} years old.".format(f_age))

def main():
    predict()


if __name__ == '__main__':
    main()
