#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
# структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
# включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
# (например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
# через заданное количество дней, вычитание заданного количества дней из даты,
# определение високосности года, присвоение и получение отдельных частей (год, месяц,
# день), сравнение дат (равно, до, после), вычисление количества дней между датами.


import datetime
from datetime import timedelta



class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Инициализация датой
    def get_vid1(self):
        vid1 = datetime.date(self.year, self.month, self.day)
        return vid1

    # Инициализация строкой
    def get_vid2(self):
        return str(Date.get_vid1(self)).replace('-', '.')

    # Инициализация числами
    def get_vid3(self):
        return f'{self.year}.{self.month}.{self.day}'

    # Вычисление даты через заданное количество дней (Сложение).
    def plusd(self, n):
        return (Date.get_vid1(self) + timedelta(days=n)).strftime("%Y.%m.%d")

    # Вычисление даты через заданное количество дней (Вычитание).
    def minusd(self, n):
        return (Date.get_vid1(self) - timedelta(days=n)).strftime("%Y.%m.%d")

    # Определение високосного года.
    def visYear(self):
        if self.year % 4 == 0:
            return 'Год является високосным!'
        else:
            return 'Год НЕ является високосным!'

    # Присвоение и получение отдельных частей даты.
    def splitdata(self):
        Y = Date.get_vid1(self).year
        M = Date.get_vid1(self).month
        D = Date.get_vid1(self).day
        return f'\n\tГод: {Y}\n\tМесяц: {M}\n\tДень: {D}'

    # Сравнение дат (равно, до, после)
    def sravnen(self):
        if date1.get_vid1() == date2.get_vid1():
            return 'Первая и вторая даты равны!'
        elif date1.get_vid1() > date2.get_vid1():
            return 'Первая дата больше второй!'
        else:
            return 'Первая дата меньше второй!'

    # Вычисление количества дней между датами.
    def daysdat(self):
        delta = date1.get_vid1() - date2.get_vid1()
        return abs(delta.days)

    # Вывод результатов
    def display(self):
        print(f"\n1) Представление даты в 3х видах:"
              f"\n\tДатой: {date1.get_vid1()}"
              f"\n\tСтрокой: {date1.get_vid2()}"
              f"\n\tЧислами: {date1.get_vid3()}")
        print(f'2) Дата после добавления заданного кол-ва дней: {date1.plusd(daysp)}')
        print(f'3) Дата после вычетания заданного кол-ва дней: {date1.minusd(daysm)}')
        print(f'4) {date1.visYear()}')  # Определение високосного года.
        print(f'5) Присвоение и получение отдельных частей даты: {date1.splitdata()}')
        print(f'6) {Date.sravnen(date1 and date2)}')  # Сравнение дат (равно, до, после)
        print(f'7) Дней между датами: {Date.daysdat(date1 and date2)}')

if __name__ == '__main__':
    # Ввод данных.
    date1 = Date(*list(map(int, input("Введите дату в формате YYYY.MM.DD: ").split('.'))))
    daysp = int(input('Сколько дней добавить к дате? '))
    daysm = int(input('Сколько дней вычесть из даты? '))
    date2 = Date(*list(map(int, input("Введите вторую дату в формате YYYY.MM.DD для сравнения с первой: ").split('.'))))

    # Вывод результатов
    Date.display(date1 and date2)

