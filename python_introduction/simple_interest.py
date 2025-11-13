def find_interest(p, r, t):
    return p * r * t

def render_interest(interest):
    print("The simple interest is {}".format(interest))

def main():
    principal = 1000
    rate = 0.05
    time = 3
    interest = find_interest(principal, rate, time)
    render_interest(interest)

if __name__ == '__main__':
    main()
