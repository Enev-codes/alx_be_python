from datetime import datetime, timedelta


def display_current_datetime(future):
    print("Future date: ", future)

def forward_time(present, delta):
    return (present + timedelta(days=delta))


def main():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date)
    days = int(input("Enter the number of days to add to the current date: "))
    future = forward_time(current_date, days)
    formatted_future = future.strftime("%Y-%m-%d")
    display_current_datetime(formatted_future)

if __name__ == '__main__':
    main()
