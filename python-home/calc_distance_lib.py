def calculate_distance(fuel_cons, fuel_rem_am):
    """
    >>> calculate_distance(10, 100)
    900
    """
    fool_factor = 0.9  # защита от дурака, занижаем фактичское оставшееся расстояние на 10%
    liters_per_km = fuel_cons / 100
    distance = fuel_rem_am / liters_per_km * fool_factor
    return round(distance)

