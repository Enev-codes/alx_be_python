def render(h, s):
    print("{}(s) hours is {} seconds.".format(h, s))

def main():
    hours = 2
    seconds = hours * 60 * 60
    render(hours, seconds)

if __name__ == '__main__':
    main()
