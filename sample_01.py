'''D = {1:[1,2,3], 2:(4,6,8)}
D[1].append(4)
print(D[1],end="")
L = D[2]
L.append(10)
D[2] = tuple(L)
print(D[2])
'''

'''
import string
Line1 = "And Then There Were None"
Line2 = "Famous In Love"
Line3 = "Famous Were The Kol And Klaus"
Line4 = Line1 + Line2 + Line3
print(string.find(Line1,'Were'),string.count((Line4),'And'))
'''
'''
value = [1,2,3,4]
data = 10
try:
    data = 10/0
except ZeroDivisionError:
    print("A")
finally:
    print("C")
'''
'''
line = "I'll come by then."
eline = ""
for i in line:
    eline += chr(ord(i)+3)
print(eline)
'''

'''
D = dict()
for i in range(3):
    for j in range(2):
        D[i] = j
print(D)
'''

'''
names = ['Abdul','Hameed','Bathusha']
bames = names
print(bames)
#print(names.append(" "))
#print(" ".join(names))
#print(names.join("%s", names))
#print(names.concatenate(""))
'''

'''
from functools import  reduce
numbers = [1,2,3]
reduce((lambda x, y:x+y, numbers))
'''

'''
def func1(name, age=20):
    print(name,age)
func1("Emma",25)
func1("Anna")
'''

'''
from math import *
a = 2.13
b = 3.7777
c = -3.123
print(int(a), floor(b), ceil(c), fabs(c))
'''

x = lambda a,b,c : a*b+c
print(x(7,7,1))
print(x(3.3,4.4,1.1))