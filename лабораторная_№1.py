# -*- coding: utf-8 -*-
"""Лабораторная №1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iLYqGinqdLTZ4gRllVNkZUO9uzjGUq65
"""

печать ( «Привет, мир» )

a=3
b=6
c=a+b
print(c)

"""Площадь равнобедренного треугольника"""

a=7.5
b=7.5
c=4

C=c/2
print(C)

h=b**2-C**2
print(h)

S=0.5*c*h
print(S)

"""Решение уравнения"""

a=2
b=1
c=3

x=(a^2+b^2-c^3)/2
print(x)

"""Самостоятельное задание

1.
"""

a=5
b=int(input())

x=a*b
print(x)

"""2."""

a=int(input())

b=int(input())

x=(a+b)**2
print(x)

x=int(input())

"""3."""

a=15
b=10
c=int(input())

x=(a+b)/c
print(x)

"""4."""

a=int(input())
b=int(input())

x=(a+b)**2
print(x)

"""5."""

a=6
b=4
c=8

P=a+b+c
p=P/2
print(P)
print(p)

S=(p*(p-a)*(p-b)*(p-c))**0.5
print(S)

"""6."""

a=2
b=1

x=((a**3+14)/5)*b
print(x)

"""7."""

x=2
n=4

h=(x**2)/n
print((x**2)//n)

"""8."""

a=float(input())
b=float(input()) 
print(a//b)

d=int(input())
i=int(input())
print(d*i)

f=int(input())
g=int(input())
print(f%g)

"""Задача повышенной сложности

1.
"""

n=6560
m=n//60
h=n//(60*60)
d=n//(60*60*12)
print(m)
print(h)
print(d)

"""2."""

n=int(input())
S1=str(n)
S2=S1*2
S3=S1*3
print(int(S1)+int(S2)+int(S3))