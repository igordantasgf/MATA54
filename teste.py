'''
f = open('dic.dat','a+')
f.seek(20)
f.write('1010')
f.seek(20)
print(f.read(4))
'''
#for i in range(1,11):
#    print(bin(i))
'''
decimais = {1:'0001',
2:'0010', 
3:'0011',
4:'0100',
5:'0101',
6:'0110',
7:'0111',
8:'1000',
9:'1001',
10:'1010'}

print('adsada'[2:4])
from classes import *
lista1 = [1,4,5]
lista2 = [6,8,9]
lista3 = [10,60,60]

a = No(lista1, None, None, None, None, None)
b = No(lista2, None, None, None, None, None)
c = No(lista3, None, None, None, None, None)
a.r = b
b.r = c
c.pai = b
'''
print(bin(32))
print(bin(97))
print(bin(122))
