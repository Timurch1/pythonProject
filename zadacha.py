def to_often(nums: str):
    max_value = 0
    symbol = ''
    for i in nums:
        counter = 0
        for b in nums:
            if i == b:
                counter += 1
        if counter > max_value:
            max_value = counter
            symbol = i
    print("Чаще всего встречается символ {0}, он встречался в строке {1} {2} раз".format(symbol, nums,
    max_value))

strochka = input("Введите слово: ")
to_often(strochka)



# Удаление повторяющихся элементов и нахождения числа неповторящихся элементов)
def to_set(nums: list):
   nums = set(nums)
   for i in range(len(nums)):
       i += 1
   print("Результат: ", i, end=', ')
   return nums

it_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 10, 10, 15, 18, 18, 20]
print(to_set(it_list))