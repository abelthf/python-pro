import datetime

my_time = datetime.datetime.now()

print(my_time)

# Output: 2022-05-13 10:58:28.654374

my_day = datetime.date.today()
print(my_day)

# Output: 2022-05-13

print(f"Year: {my_day.year}")
print(f"Month: {my_day.month}")
print(f"Day: {my_day.day}")

"""
Output:
Year: 2022
Month: 5
Day: 13

"""
