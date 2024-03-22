# Нахождение количества определенных символов в строке

def search_symwal(stroka,symwal: str):
    res = 0
    for i in stroka:
        if i== symwal:
            res += 1
    print("Количество",symwal,':', res)
    return stroka

stroka= str(input("Введите слово: "))
symwal = str(input("Введите символ: "))
count = search_symwal(stroka, symwal)
print(count)