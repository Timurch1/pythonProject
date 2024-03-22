# Задача на поиск количества цифр в строке
def to_int_stroka(nums: str) -> int:
    res = 0
    for i in nums:
        if '0' <= i <= '9':
            res += 1
    return res


# Нахождение количества символа в строке
def search_symwal(stroka: str):
    res = 0
    for i in stroka:
        if i == symwal:
            res += 1
    print("Количество",symwal,':', res)
    return stroka

stroka= str(input("Введите слово: "))
symwal = str(input("Введите символ: "))
count = search_symwal(stroka)
print(count)