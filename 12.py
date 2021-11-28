# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar

def draw_cal(yy, mm):
    print(calendar.month(yy, mm))

yy = int(input("Write a year: "))
mm = int(input("Write a month: "))
draw_cal(yy, mm)
