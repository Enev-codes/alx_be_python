def main():
    # Prompt user for data
    m_income = int(input("Enter your monthly income: "))
    m_expens = int(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    m_savings = m_income - m_expens

    # Project annual savings
    rate = 0.05
    time = 1
    interest = m_savings * rate * time
    pm_savings = m_savings + interest
    pa_savings = pm_savings * 12       # projected annual savings
    print("Your monthly savings are {}\nProjected savings after one year, with interest, is: {}".format(int(m_savings), int(pa_savings)))


if __name__ == '__main__':
    main()
