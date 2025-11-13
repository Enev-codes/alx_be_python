def calc_area(l, w):
    return l * w

def render_area(area):
    print("The area of the rectangle is: {}".format(area))

def main():
    length = 10
    width = 5
    area = calc_area(length, width)
    render_area(area)


if __name__ == '__main__':
    main()
