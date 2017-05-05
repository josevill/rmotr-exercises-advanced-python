from datetime import datetime

date_test = datetime(2016, 1, 5, 13, 30)

def format_datetime(dt):
    # Creating a datetime object from the input
    formated_date = dt.strftime("%A %B %d, %Y at %I:%M hs")
    print(formated_date)

format_datetime(date_test)
