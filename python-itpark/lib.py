def cashback(monthly_expenses):
    """
    >>> cashback(10000)
    300.0
    """
    persent = 3
    result = persent * monthly_expenses / 100
    return result


def bmi(weight, height):
    """
    >>> bmi(106, 1.68)
    37.56
    """
    index = weight / (height * height)
    return round(index, 2)
