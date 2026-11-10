# -*- coding: utf-8 -*-
"""Самостійна робота №1: консольна програма зі структурами даних."""
import math
VALUES = [3, 6, 9, 12, 15]
N = 6
R = 4

def factorial(n):
    if n<0:raise ValueError('Число має бути невід’ємним')
    result=1
    for k in range(2,n+1):result*=k
    return result

def area(kind,value):
    if value<=0:raise ValueError('Розмір має бути додатним')
    if kind=='коло':return math.pi*value**2
    if kind=='квадрат':return value**2
    raise ValueError('Невідома фігура')

class NumberIterator:
    def __init__(self,items):self.items=items;self.index=0
    def __iter__(self):return self
    def __next__(self):
        if self.index>=len(self.items):raise StopIteration
        value=self.items[self.index];self.index+=1;return value

def even_numbers(items):
    for number in items:
        if number%2==0:yield number

def main():
    values=VALUES
    print('Список:',values,'кортеж:',tuple(values))
    print('Словник квадратів:',{x:x*x for x in values})
    print('Факторіал:',factorial(N),'Площа кола:',round(area('коло',R),2))
    print('Ітератор:',list(NumberIterator(values)))
    print('Генератор парних:',list(even_numbers(values)))
    print('Генераторний вираз:',sum(x*x for x in values))
    print('Умови:', ['парне' if x%2==0 else 'непарне' for x in values])
if __name__=='__main__':main()
