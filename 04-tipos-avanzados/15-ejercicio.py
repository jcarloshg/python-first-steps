

def drop_white_spaces(value: str) -> str:
    # new_string = ""
    # for char in value:
    #     if char != " ":
    #         new_string += char
    # return new_string
    return [char for char in value if char != " "]


def counting_chart(value: str) -> dict:
    chars = {}
    for char in value:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_dictionaries(dictonary: dict):
    # new_list = []
    # for item in dictonary.items():
    #     new_list.append(item)
    # new_list.sort(key=lambda item: item[1])
    # return new_list
    return sorted(
        dictonary.items(),
        key=lambda item: item[1],
        reverse=True
    )


def get_greatest_value(list_sorted: list) -> list:
    print(list_sorted)
    major_value = list_sorted[0]
    list_filtered = list(
        filter(lambda item: item[1] == major_value[1], list_sorted))
    return list_filtered


def print_greatest_values(list_values: list) -> list:
    for item in list_values:
        print(f"el char: {item[0]} se repite {item[1]}")


string = "Anita lava la tina"
sin_espacios = drop_white_spaces(string)
print(sin_espacios)
# ['A', 'n', 'i', 't', 'a', 'l', 'a', 'v', 'a', 'l', 'a', 't', 'i', 'n', 'a']

chart_counting = counting_chart(sin_espacios)
print(chart_counting)
# {'A': 1, 'n': 2, 'i': 2, 't': 2, 'a': 5, 'l': 2, 'v': 1}

chart_counting_sorted = sort_dictionaries(chart_counting)
print(chart_counting_sorted)
# [('A', 1), ('v', 1), ('n', 2), ('i', 2), ('t', 2), ('l', 2), ('a', 5)]

majors_values = get_greatest_value(chart_counting_sorted)
print(majors_values)

print_greatest_values(majors_values)
