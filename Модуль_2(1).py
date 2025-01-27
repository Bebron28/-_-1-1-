#Задание1
a = int(input("Введите число "))
b = int(input("Введите число "))
c = int(input("Введите число "))
v = int(input("выберите сумму(1) или произведение(2):"))
if v == 1:
    print("Сумма:", a+b+c)
elif v == 2:
    print("произведение:", a*b*c)

#Задание2
q = int(input("Введите число "))
w = int(input("Введите число "))
e = int(input("Введите число "))
r = int(input("выберите максимальное(1), минимальное(2) или среднеарифметическое(3):"))
if r == 1:
    print(max(q, w, e))
elif r == 2:
    print(min(q, w, e))
elif r == 3:
    print((q + w + e) / 3)

#Задание3
metr = int(input("Введите колво метров "))
choose = int(input("Перевести в мили(1), дюймы(2) или в ярды(3) "))
if choose == 1:
    print("Милей: ", metr / 1609)
elif choose == 2:
    print("Дюймов: ", metr * 39.37)
elif choose == 3:
    print("Ярдов: ", metr * 1.094)
        
