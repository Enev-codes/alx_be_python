from datetime import datetime, timedelta


def display_current_datetime(present):
    print("Current date and time: ", present)

def display_future_datetime(future):
    print("Future date: ", future)

def calculate_future_date(present, delta):
    return (present + timedelta(days=delta))


def main():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    display_current_datetime(formatted_date)
    days = int(input("Enter the number of days to add to the current date: "))
    future = calculate_future_date(current_date, days)
    formatted_future = future.strftime("%Y-%m-%d")
    display_future_datetime(formatted_future)

if __name__ == '__main__':
    main()
