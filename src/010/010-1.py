def is_leap(year):
  """ returns True/False for int year """
  if year % 4 == 0:
    return True
    if year % 100 == 0:
      return True
      if year % 400 == 0:
        return True
  else:
    return False

def days_in_month(yr, mo):
  """ returns the days in a month accounting for leap year """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  mo = mo - 1
  leap_yr = is_leap(yr)
  if leap_yr == True and mo == 1:
    return int(month_days[mo] + 1)
  else:
    return int(month_days[mo])

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
