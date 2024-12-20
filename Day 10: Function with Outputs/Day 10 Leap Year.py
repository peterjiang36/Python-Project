def is_leap_year(year):
    """ A function that consider if the year is a leap year or not
    :param year: integer that representing the year
    :return:
    """
    if year % 4 == 0:
        # return ("divided by 4 has no reminder")
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(is_leap_year(2100))
