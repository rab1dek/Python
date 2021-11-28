# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import datetime
from datetime import date

def calculate_date(fd,sd):
    return sd - fd

first_date = datetime.datetime(2014,7,2)
second_date = datetime.datetime(2014,7,11)
print(calculate_date(first_date, second_date).days)

