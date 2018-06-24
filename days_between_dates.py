daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countLeapYear(year, month):
    
    # check for current year to be considered for the count of leap years or not
    if month <= 2:
        year -= 1

    # multiple of 4, multiple of 400 and not a multiple of 100 is a leap year
    return year / 4 - year / 100 + year / 400

def countDaysBefore(year, month, day):
    
    # Count year and day
    days = year * 365 + day

    # Add days for month in given date
    for i in range(month):
        days += daysOfMonth[i]

    # Add day for every leap year
    days += countLeapYear(year, month)

    return days

def days_between_dates(y1, m1, d1, y2, m2, d2):
    """
    Calculates the number of days between two dates.
    """
    # Count total number of days before first date
    days1 = countDaysBefore(y1, m1, d1)

    # Count total number of days before second date
    days2 = countDaysBefore(y2, m2, d2)
    
    # return difference between two days
    return days2 - days1

def test_days_between_dates():
    
    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(days_between_dates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")
    
test_days_between_dates()
