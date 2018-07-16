def selection_sort(list):
    initial_position = 0
    lowest_value_position = 0

    while(initial_position < len(list)):
        for x in range(initial_position, len(list)):
            if(list[x] < list[lowest_value_position]):
                lowest_value_position = x
        list[initial_position], list[lowest_value_position] = list[lowest_value_position], list[initial_position]
        initial_position += 1
        lowest_value_position = initial_position

    return list
