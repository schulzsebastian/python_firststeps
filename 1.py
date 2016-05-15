"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

l = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print " ".join(l)

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

    x = [int(i) for i in raw_input().split(" ")]
    l = []
    for i in x:
        c = i
        while c > 1:
            c -= 1
            i *= c
        l.append(str(i))
    print " ".join(l)

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

x = int(raw_input())
d = {}
for i in range(1, x+1):
    d[i] = i*i
print d

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

liczby = raw_input("podaj liczby: ")
lista = list(liczby.split(","))
tupla = tuple(liczby.split(","))
print lista
print tupla

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

class klasa(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = klasa()
strObj.getString()
strObj.printString()

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

import math
x = [int(i) for i in raw_input().split(" ")]
l = []
for i in x:
    l.append(str(int(math.sqrt(2*50*i/30))))
print " ".join(l)

#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print ','.join(value)


Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world


l = [i for i in raw_input().split(" ")]
print " ".join(sorted(l))

rite a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

l = []
while True:
    x = raw_input()
    if x:
        l.append(x.upper())
    else:
        break
for i in l:
    print i
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

x = [i for i in raw_input().split(" ")]
l = []
for i in x:
    if i in l:
        continue
    l.append(i)
print " ".join(sorted(l))

s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

l = []
for i in range(1000,3001):
    c = 0
    for j in str(i):
        if int(j)%2!=0:
            c+=1
    if c==4:
        l.append(str(i))
print " ".join(l)

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)


Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

2. isalpha() & isdigit()
x = raw_input()
d = {"d":0, "l":0}
for i in x:
    if i.isdigit():
        d["d"]+=1
    elif i.isalpha():
        d["l"]+=1
print "digits:",d["d"],"letters:",d["l"]

l = [i for i in raw_input().split(" ") if int(i)%2!=0]
print " ".join(l)

b = 0
while True:
    x = raw_input()
    if x:
        x = x.split(" ")
        if x[0]=="W":
            b -= int(x[1])
        elif x[0]=="D":
            b += int(x[1])
        else:
            pass
    else:
        print b
        break



import re
l = []
x = raw_input().split(" ")
for i in x:
    if len(i)>=6 or len(i)<=12:
        if (re.search("[a-z]",i) and re.search("[A-Z]",i) and re.search("[0-9]",i)
            and re.search("[$#@]",i) and not re.search("\s",i)):
            l.append(i)
print " ".join(l)

from operator import itemgetter
t = ()
l = []
while True:
    t = raw_input()
    if t:
        l.append(t.split(","))
    else:
        break
print sorted(l,key=itemgetter(0,1,2))

def generatorbyseven(x):
    l = []
    for i in range(0,x+1):
        if i%7 == 0:
            l.append(str(i))
    return l
x = int(raw_input())
print " ".join(generatorbyseven(x))

def generatoryield(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in putNumbers(100):
    print i

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

pos = [0,0]
while True:
    x = raw_input()
    if x:
        x = x.split(" ")
        direction = x[0]
        steps = int(x[1])
        if direction == "UP":
            pos[1]+=steps
        elif direction == "DOWN":
            pos[1]-=steps
        elif direction == "RIGHT":
            pos[0]+=steps
        elif direction == "LEFT":
            pos[0]-=steps
        else:
            pass
    else:
        break
print pos

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

d = {}
x = raw_input()
for w in x.split(" "):
    d[w] = d.get(w,0)+1
k = d.keys()
k.sort()
for w in k:
    print w+":",d[w]

class rectangle(object):
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width
    def o(self):
        return self.length*2+self.width*2

prostokat = rectangle(5,5)

print prostokat.area()
print prostokat.o()


Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        self.length = l
    def area(self):
        return self.length**2

a = Square(-1)
print a.area()

"""
while True:
    x = raw_input()
    if x:
        x = float(x)
        print x*100/204300.0
    else:
        break