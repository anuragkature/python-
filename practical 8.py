from datetime import datetime, timedelta
# Function to get current date and time
def get_current_date_time():
    return datetime.now()
# Function to get current date only
def get_current_date():
    return datetime.now().date()
# Function to add some days to the current date
def add_days_to_date(date, num_days):
    return date + timedelta(days=num_days)
current_date_time = get_current_date_time()
print("Current date and time: ", current_date_time)
num_days = int(input("Enter the number of days to add to the current date: "))
new_date = add_days_to_date(get_current_date(), num_days)
print("Date after adding ", num_days, " days: ", new_date)
current_date = get_current_date()
print("Current date only: ", current_date)
date_time = get_current_date_time()
print("Date and time using date and time functions: ", date_time.date(), date_time.time())