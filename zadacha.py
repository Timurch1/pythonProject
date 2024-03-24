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