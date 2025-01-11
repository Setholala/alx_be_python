from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)



def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = timedelta(days=number_of_days) + current_date
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(formatted_date)

    
display_current_datetime()

number_of_days = int(input("Enter number of days: "))

calculate_future_date(number_of_days)

