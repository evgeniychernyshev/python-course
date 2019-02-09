roll_length = float(input('Enter roll length (m): '))
roll_width = float(input('Enter roll width (m): '))
room_length = float(input('Enter room length (m): '))
room_width = float(input('Enter room width (m): '))
ceiling_height = float(input('Enter ceiling height (m): '))


# считаем общее кол-во рулонов
def calculate_rolls_count(roll_l, roll_w, room_l, room_w, ceiling_h):
    room_perimeter = calculate_perimeter(room_l, room_w)
    canvas_count = calculate_canvas_count(room_perimeter, roll_w)
    canvas_in_roll = calculate_canvas_in_roll(roll_l, ceiling_h)
    rolls_count_total = canvas_count / canvas_in_roll
    rest = canvas_count % canvas_in_roll
    if rest > 0:
        return canvas_count // canvas_in_roll + 1
    else:
        return rolls_count_total


# считаем периметр комнаты
def calculate_perimeter(room_l, room_w):
    return (room_l + room_w) * 2


# считаем общее кол-во полотнищ на комнату
def calculate_canvas_count(perimeter, roll_w):
    count = perimeter / roll_w
    rest = perimeter % roll_w
    if rest > 0:
        return perimeter // roll_w + 1  # округляем количество полотнищ в большую сторону
    else:
        return count


# считаем кол-во полотнищ в 1 рулоне
def calculate_canvas_in_roll(roll_l, ceiling_h):
    fund = 0.1  # добавляем к высоте потолка 10см прозапас
    return roll_l // (ceiling_h + fund)


rolls_count = calculate_rolls_count(roll_length, roll_width, room_length, room_width, ceiling_height)
print('You need', rolls_count, 'rolls. We recommend buy 1-2 rolls more.')
