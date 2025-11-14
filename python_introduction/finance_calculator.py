def render(m_sav, pa_sav):
    print("Your monthly savings are {}\nProjected savings after one year, with interest, is: {}".format(m_sav, pa_sav))


def main():
    # Prompt user for data
    m_income = int(input("Enter your monthly income: "))
    m_expens = int(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    m_savings = m_income - m_expens

    # Project annual savings
    rate = 5
    time = 1
    interest = m_savings * (rate / 100) * (time)
    pm_savings = m_savings + interest
    pa_savings = pm_savings * 12       # projected annual savings
    render(int(m_savings), int(pa_savings))


if __name__ == '__main__':
    main()
