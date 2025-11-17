from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    now = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(now)

def main():
    display_current_datetime()

if __name__ == '__main__':
    main()
