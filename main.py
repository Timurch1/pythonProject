def find_longest_substring(stroka):
    podstroka = set(stroka)
    return podstroka


def ilya_solution(value):
    output = ""
    max_length = 0
    used_chars = []

    for i in range(len(value)):
        if value[i] in used_chars:
            if len(used_chars) > max_length:
                max_length = len(used_chars)
                output = ""
                for s in used_chars:
                    output = output + s
                used_chars.clear()
        else:
            used_chars.append(value[i])
    return output


# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Задание : программа должна перевести римские цифры в обычные десятичные в формате int.
# Например :
# "III" == 3
# "LVIII" == 58
# "MCMXCIV" == 1994
# @roman - римское число
def roman_to_int(roman):
    pass


# Дан отсортированный массив целых чисел nums и число target. Функция должна вернуть индекс
# числа target в массиве, а если этого числа нет, то индекс предпологаемого места в массиве.
def search_insert_position(nums, target):
    pass
