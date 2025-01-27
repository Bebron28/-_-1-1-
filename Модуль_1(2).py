#Задание1
a = input("введите цифру")
b = input("введите цифру")
c = input("введите цифру")
print(a + b + c)

#Задание2
q = int(input("введите четырехзначное число:"))
first = q // 1000
second = (q % 1000) // 100
third = (q % 100) // 10
fourth = q % 10
print(first * second * third * fourth)

#Задание3
metr = int(input("введите колво метров:"))
sm = metr * 100
dm = metr * 10
ml = metr * 1000
mili = metr / 1610
print(sm, "\n", dm, "\n", ml, "\n", mili)

#Задание4
A = int(input("введите основание треугольника: "))
h = int(input("введите высоту треугольника: "))
S = A * h / 2
print(S)

#Задание5
numb = input("введите четырехзначное число:")
print(numb[::-1])
