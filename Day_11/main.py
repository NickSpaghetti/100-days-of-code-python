year = int(input("What year is it?"))

is_leap_year = year // 4 == 0
print(is_leap_year)

seconds_per_day = pow(60, 2) * 24
seconds_per_year = 0
if (is_leap_year):
    seconds_per_year = seconds_per_day * 366
else:
    seconds_per_year = seconds_per_day * 365

print("Thre are {0} seconds in the year {1}".format(seconds_per_year, year))
