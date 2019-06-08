def find_max(list):
    biggest_number = list[0]
    for item in list[1:]:
        if biggest_number < item:
            biggest_number = item
    return biggest_number