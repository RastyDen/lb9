#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа в данной
# степени.

class Number:
    def __init__(self, a, b):
        self.numa = float(a)
        self.numb = float(b)

    # Вычесление произведения чесел a и b
    def umn(self):
        self.aub = self.numa * self.numb
        return self.aub

    # Вычесление разницы чесел a и b
    def vichet(self):
        self.amb = self.numa - self.numb
        return self.amb

class Real(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

    # Вычесление корня произвольной степени для произведения чесел a и b
    def korumn(self, n):
        kor = pow(Number.umn(self), (1 / n))
        return kor

    # Вычесление корня произвольной степени для разницы чесел a и b
    def korvichet(self, n):
        kor = pow(Number.vichet(self), (1 / n))
        return kor

    # Вычесление произведения чесел a и b в данной степени
    def stepumn(self, n):
        step = Number.umn(self)**n
        return step

    # Вычесление разницы чесел a и b в данной степени
    def stepvichet(self, n):
        step = Number.vichet(self)**n
        return step

    # Вывод результатов
    def display(self):
        print(f'1) Произведение чесел a и b: {par1.umn()}')
        print(f'2) Разница чесел a и b: {par1.vichet()}')
        print(f'3) Корень произвольной степени для произведения чесел a и b: {Real(a, b).korumn(n)}')
        print(f'4) Корень произвольной степени для разницы чесел a и b: {Real(a, b).korvichet(n)}')
        print(f'5) Произведение чесел a и b в степени {n}: {Real(a, b).stepumn(n)}')
        print(f'6) Разница чесел a и b в степени {n}: {Real(a, b).stepvichet(n)}')

if __name__ == '__main__':
    # Ввод данных.
    a = input('Введите число a: ')
    b = input('Введите число b: ')
    par1 = Number(a, b)
    n = float(input("Введите степень: "))

    # Вывод результатов.
    Real(a, b).display()



