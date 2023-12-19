def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    return max_value


def list_min(input_list):
    min_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] < min_value:
            min_value = input_list[i]

    return min_value
