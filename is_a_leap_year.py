def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Year is divisible by 400
            else:
                return False  # Year is divisible by 100 but not by 400
        else:
            return True  # Year is divisible by 4 but not by 100
    else:
        return False  # Year is not divisible by 4
is_leap_year(2001)