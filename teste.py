'''
f = open('dic.dat','a+')
f.seek(20)
f.write('1010')
f.seek(20)
print(f.read(4))
'''
#for i in range(1,11):
#    print(bin(i))
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