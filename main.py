# Нахождение числа цифр в строке
def to_int_stroka(nums: str) -> int:
    res = 0
    for i in nums:
         if i == '0':
            res += 1
         elif i == '2':
             res += 1
         elif i == '3':
             res += 1
         elif i == '4':
             res += 1
         elif i == '5':
             res += 1
         elif i == '6':
             res += 1
         elif i == '7':
             res += 1
         elif i == '8':
             res += 1
         elif i == '9':
             res += 1
    print("Количество цифр: ", res)
    return nums
stroka = input("Введите слово: ")
count = to_int_stroka(stroka)
print('Наше слово:', count)