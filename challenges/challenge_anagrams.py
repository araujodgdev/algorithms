def my_merge_sort(input_str):
    if len(input_str) <= 1:
        return input_str

    middle = len(input_str) // 2
    left_half = input_str[:middle]
    right_half = input_str[middle:]

    left_sorted = my_merge_sort(left_half)
    right_sorted = my_merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left_str, right_str):
    result = []
    i = j = 0

    while i < len(left_str) and j < len(right_str):
        if left_str[i] < right_str[j]:
            result.append(left_str[i])
            i += 1
        else:
            result.append(right_str[j])
            j += 1

    result.extend(left_str[i:])
    result.extend(right_str[j:])

    return ''.join(result)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string = my_merge_sort(first_string)
    second_string = my_merge_sort(second_string)

    if first_string == "" or second_string == "":
        return tuple((first_string, second_string, False))

    if first_string == second_string:
        return tuple((first_string, second_string, True))
    else:
        return tuple((first_string, second_string, False))
