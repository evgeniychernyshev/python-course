fuel_consumption = float(input('Enter fuel consumption (liters per 100 km): '))
fuel_remaining_amount = float(input('Enter fuel remaining amount: '))


def calculate_distance(fuel_cons, fuel_rem_am):
    fool_factor = 0.9  # защита от дурака, занижаем фактичское оставшееся расстояние на 10%
    liters_per_km = fuel_cons / 100
    distance = fuel_rem_am / liters_per_km * fool_factor
    return round(distance)


distance = calculate_distance(fuel_consumption, fuel_remaining_amount)
print('Remaining distance is', distance)