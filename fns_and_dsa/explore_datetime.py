from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    
    return current_date

number_of_days = int(input("Enter number of days: "))

def calculate_future_date(number_of_days):
    future_date = timedelta(days=number_of_days) + display_current_datetime()

display_current_datetime()
calculate_future_date(number_of_days)

