from calc_distance_lib import calculate_distance

fuel_consumption = float(input('Enter fuel consumption (liters per 100 km): '))
fuel_remaining_amount = float(input('Enter fuel remaining amount: '))
distance = calculate_distance(fuel_consumption, fuel_remaining_amount)
print('Remaining distance is', distance, 'km')