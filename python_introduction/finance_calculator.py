def main():
    # Prompt user for data
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Project annual savings
    rate = 0.05
    time = 1
    interest = m_savings * (time * 12) * rate
    pa_savings = m_savings * (time * 12) + interest # pas
    print("Your monthly savings are ${}.\nProjected savings after one year, with interest, is: ${}.".format(float(m_savings), float(pa_savings)))


if __name__ == '__main__':
    main()
