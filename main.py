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