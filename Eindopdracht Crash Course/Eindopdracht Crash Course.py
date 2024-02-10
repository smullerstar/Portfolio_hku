# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:07:20 2024

@author: brams
"""
# 1 opdracht 
import random as ran
import numpy as np
import matplotlib.pyplot as plt

def dobbel (amount, min_, max_):
    x = []
    for i in range(amount):
        y =  ran.randint(min_, max_)
        x.append(y)
    return(x)

print(f'b: Als er een dobbelsteen wordt gegooit komt er {dobbel(1,1,6)[0]}')

dobbel_2 = []

for i in range(50):
    z = dobbel(2, 1, 6)
    dobbel_2.append(sum(z))

dobbelsum = sum(dobbel_2)

print(f'c: Na het gooien van twee dobbelstenen 50 komt {dobbelsum}')

gem_dobbel = round(np.average(dobbel_2))  

print(f'd: Het gemidelde van 50 keer twee dobbelstenen gooien is {gem_dobbel}')

dobbel_1 = dobbel(50, 1, 6)
print(f'e: Als er 50 keer een dobbelsteen wordt gegooit kan er de volgende lijst uit komen: {dobbel_1}')

print(f'f: Het 20ste element van de boven staande lijst is {dobbel_1[19]}')

plt.figure(1)
plt.hist(dobbel_1,bins=6)
plt.ylabel('Aantal [~]')
plt.xlabel('Gooi [~]')
plt.title('g: Histogram van 50 dobbelstenen')
plt.show()

# opdracht 2
def f(x):
    y = np.pi * np.exp(-2*x)
    return y

def g(x):
    y = np.tan(2 * (x**2) + 30)
    return y

def h(x):
    y = (np.sin(3 * x) ** 2) + (np.cos(x) ** 2)
    return y

x = np.linspace(0, 10, 1000)

fig, ax = plt.subplots()  
plt.title('Opdracht 2: wiskundige vergelijkingen')
ax2 = ax.twinx()
ax.plot(x, f(x), label='f(x)', color = 'r')
ax2.plot(x, g(x), label='g(x)', color = 'b')
ax.plot(x, h(x), label='h(x)', color = 'g')
ax.set_xlabel('x-as')
ax.set_ylabel('y-as1')  
ax2.set_ylabel('y-as2') 
ax.legend(loc = 'upper left')
ax2.legend(loc = 'upper right')
plt.show()


