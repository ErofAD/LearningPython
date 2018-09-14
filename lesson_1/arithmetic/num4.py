'''В зависимости от того, что выберет пользователь, вычислить площадь либо прямоугольника,
либо треугольника, либо круга. Если выбраны прямоугольник или треугольник, то надо запросить
длины сторон, если круг, то его радиус.'''
from math import pi

def checkInput(a):
    num = input('Введите сторону %s = ' % a)
    if num[0] == '-':
        return 0
    else:
        return float(num)

def num4():
    print('Выберите фигуру:\n   1) Прямоугольник\n   2) Треугольник\n   3) Круг')
    select = int(input())
    if select == 1:
        a = checkInput('a')
        b = checkInput('b')
        if a > 0 and b > 0:
            print('S = ', round(a * b, 2))
        else:
            print('Введены некорректные данные')
    elif select == 2:
        a = checkInput('a')
        b = checkInput('b')
        c = checkInput('c')
        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c)/2
                print('S = ', round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2))
            else:
                print('Треугольник не существует')
        else:
            print('Введены некорректные данные')
    elif select == 3:
        r = checkInput('r')
        if r > 0:
            print('S = ', round(pi * r ** 2, 2))
        else:
            print('Введены некорректные данные')
    else:
        print('Неправильно ввели номер, попробуйте еще раз')
        num4()

if __name__ == "__main__":
    num4()