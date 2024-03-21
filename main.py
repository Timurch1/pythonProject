# Удаление повторяющихся элементов и нахождения числа неповторящихся элементов)
def to_set(nums: list):
   nums = set(nums)
   for i in range(len(nums)):
       i += 1
   print("Результат: ", i, end=', ')
   return nums

it_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 10, 10, 15, 18, 18, 20]
print(to_set(it_list))





# Нахождение количества символов в строке)

stroka = input("Enter str = ")
for i in set(stroka):
    stroka.count(i)
    print(i,'= is', stroka.count(i))