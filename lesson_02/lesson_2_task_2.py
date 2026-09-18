def is_year_leap(year):
    result = 'год ' + str(year) + ': '
    print(result + str(year % 4 == 0))


is_year_leap(2021)
