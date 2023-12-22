#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для своего индивидуального задания лабораторной работы 2.23 необходимо организовать
# конвейер, в котором сначала в отдельном потоке вычисляется значение первой функции,
# после чего результаты вычисления должны передаваться второй функции, вычисляемой в
# отдельном потоке. Потоки для вычисления значений двух функций должны запускаться одновременно.

import threading
import math

class Function1(threading.Thread):
    def __init__(self, x, epsilon):
        threading.Thread.__init__(self)
        self.x = x
        self.epsilon = epsilon
        self.result = 0

    def run(self):
        n = 0
        term = (self.x ** (2 * n)) / math.factorial(2 * n)
        while abs(term) > self.epsilon:
            self.result += term
            n += 1
            term = (self.x ** (2 * n)) / math.factorial(2 * n)

class Function2(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value
        self.result = 0

    def run(self):
        # Пример второй функции: экспоненциальная функция от значения первой функции
        self.result = math.exp(self.value)

def main():
    x = 1/2
    epsilon = 1e-7

    thread1 = Function1(x, epsilon)

    thread2 = Function2(0)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    result1 = thread1.result
    result2 = thread2.result

    print(f"Результат первой функции: {result1}")
    print(f"Результат второй функции: {result2}")

if __name__ == "__main__":
    main()
