#Задание1
a = int(input("Введите номер дня недели(1-7) "))
if a == 1:
    print("Понедельник")
elif a == 2:
    print("Вторник")
elif a == 3:
    print("Среда")
elif a == 4:
    print("Четверг")
elif a == 5:
    print("Пятница")
elif a == 6:
    print("Суббота")
elif a == 7:
    print("Воскресенье")

#Задание2
b = int(input("Введите номер месяца(1-12) "))
if b == 1:
    print("Январь")
elif b == 2:
    print("Февраль")
elif b == 3:
    print("Март")
elif b == 4:
    print("Апрель")
elif b == 5:
    print("Май")
elif b == 6:
    print("Июнь")
elif b == 7:
    print("Июль")
elif b == 8:
    print("Август")
elif b == 9:
    print("Сентябрь")
elif b == 10:
    print("Октябрь")
elif b == 11:
    print("Ноябрь")
elif b == 12:
    print("Декабрь")

#Задание3
c = int(input("Введите число "))
if c > 0:
    print("Number is positive")
elif c < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

#Задание4
q = int(input("Введите чиcло "))
w = int(input("Введите число "))
if q == w:
    print("Числа равны")
else:
    if q > w:
        q, w = w, q
        print(q, w)
    else:
        print(q, w)
