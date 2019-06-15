Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=(11,22)
>>> d={'name':'prateek','Course':'MCA','College',:'VIPS'}
SyntaxError: invalid syntax
>>> d={'name':'prateek','Course':'MCA','College':'VIPS'}
>>> d.keys()
dict_keys(['name', 'Course', 'College'])
>>> d.values()
dict_values(['prateek', 'MCA', 'VIPS'])
>>> d.items()
dict_items([('name', 'prateek'), ('Course', 'MCA'), ('College', 'VIPS')])
>>> for i in d:
	print(i)

	
name
Course
College
>>> fir i,j in d.items():print(i,'is',j)
SyntaxError: invalid syntax
>>> 
>>> for i,j in d.items():print(i,'is',j)

name is prateek
Course is MCA
College is VIPS
>>> type(d)
<class 'dict'>
>>> for i in d.items():print(i)

('name', 'prateek')
('Course', 'MCA')
('College', 'VIPS')
>>> a,b=('hello','world')
>>> s
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
'hello'
>>> b
'world'
>>> 
>>> 
================= RESTART: C:/Python/Python37-32/Day 7/1.py =================
<class 'dict'>
{'Name': 'Trng', 'Age': 7, 'Class': 'First'}
Traceback (most recent call last):
  File "C:/Python/Python37-32/Day 7/1.py", line 4, in <module>
    print("keys",dict1.key())
AttributeError: 'dict' object has no attribute 'key'
>>> 
================= RESTART: C:/Python/Python37-32/Day 7/1.py =================
<class 'dict'>
{'Name': 'Trng', 'Age': 7, 'Class': 'First'}
keys dict_keys(['Name', 'Age', 'Class'])
values dict_values(['Trng', 7, 'First'])
items dict_items([('Name', 'Trng'), ('Age', 7), ('Class', 'First')])
dict['Name']: Trng
dict['Age']: 7
>>> d1={1:"one",2:"two"}
>>> print(d1.values())
dict_values(['one', 'two'])
>>> print(d1.keys())
dict_keys([1, 2])
>>> d1.clear()
>>> print(d1)
{}
>>> d1={1:"one",2:"two"}
>>> d2=d1.copy()
>>> print(id(d1))
50316464
>>> print(id(d2))
47826288
>>> print(d1.get(1))
one
>>> print(d1.get(2))
two
>>> print(d1.get("one"))
None
>>> print(d1.get(33))
None
>>> print(d1.items())
dict_items([(1, 'one'), (2, 'two')])
>>> print(d1.keys())
dict_keys([1, 2])
>>> print(d1)
{1: 'one', 2: 'two'}
>>> print('After popping',d1.pop())
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print('After popping',d1.pop())
TypeError: pop expected at least 1 arguments, got 0
>>> print('After popping',d1.pop(1))
After popping one
>>> print(d1)
{2: 'two'}
>>> print(d1.pop(2))
two
>>> print(d1)
{}
>>> print('After popping two',di.pop(1))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print('After popping two',di.pop(1))
NameError: name 'di' is not defined
>>> print('After popping two',d1.pop(1))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print('After popping two',d1.pop(1))
KeyError: 1
>>> print('After popping two',d1.pop(2,100))
After popping two 100
>>> d1={1:"one",2:"two"}
>>> print(d1.popitem())
(2, 'two')
>>> print(d1)
{1: 'one'}
>>> d1={1:"one",2:"two"}
>>> print(d1)
{1: 'one', 2: 'two'}
>>> d1.get(5)
>>> x=d1.get(5)
>>> x
>>> print(x)
None
>>> print(d1.get(2))
two
>>> print(d1)
{1: 'one', 2: 'two'}
>>> print(d1.pop(2))
two
>>> print(d1)
{1: 'one'}
>>> d1={1:"one",2:"two"}
>>> a=dict('one'=1,'two'=2,'three'=3)
SyntaxError: keyword can't be an expression
>>> a=dict(one=1,two=2,three=3)
>>> print("a:",a)
a: {'one': 1, 'two': 2, 'three': 3}
>>> b={'one':1,'two':2,'three':3}
>>> print("b:",b)
b: {'one': 1, 'two': 2, 'three': 3}
>>> print(len(a))
3
>>> print(d['two'])
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(d['two'])
NameError: name 'd' is not defined
>>> print(b['two'])
2
>>> c=dict(zip(['one','two','three'],[10,20,30]))
>>> print("content is",c)
content is {'one': 10, 'two': 20, 'three': 30}
>>> print(dict([('two',2),('one',1),('three',3)]))
{'two': 2, 'one': 1, 'three': 3}
>>> print(dict({'three':3,'one':1,'two':2}))
{'three': 3, 'one': 1, 'two': 2}
>>> d=dict({'three':3,'one':1,'two':2})
>>> print(d)
{'three': 3, 'one': 1, 'two': 2}
>>> e=dict([('two',2),('one',1),('three',3)]))
SyntaxError: invalid syntax
>>> e=dict([('two',2),('one',1),('three',3)])
>>> print(e)
{'two': 2, 'one': 1, 'three': 3}
>>> print(a==b==c==d==e)
False
>>> print(len(a))
3
>>> print(d['two'])
2
>>> a=dict(one=1,two=2,three=3)
>>> f={}
>>> print(f.fromkeys(a))
{'one': None, 'two': None, 'three': None}
>>> g={5:'five',6:'six'}
>>> a
{'one': 1, 'two': 2, 'three': 3}
>>> a.fromkeys(g)
{5: None, 6: None}
>>> a
{'one': 1, 'two': 2, 'three': 3}
>>> a=a.fromkeys(g)
>>> a
{5: None, 6: None}
>>> print(a)
{5: None, 6: None}
>>> d1={0:10,1:20}
>>> print(d1)
{0: 10, 1: 20}
>>> d1[2]=30
>>> d1
{0: 10, 1: 20, 2: 30}
>>> d1['name']='arshdeep'
>>> print(d1)
{0: 10, 1: 20, 2: 30, 'name': 'arshdeep'}
>>> d1[0]=100
>>> print(d1)
{0: 100, 1: 20, 2: 30, 'name': 'arshdeep'}
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
============ RESTART: C:/Python/Python37-32/Day 7/colorchoice.py ============
0:blue
1:red
2:orange
3:yellow
4:quit
select a color option2
you chose orange!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option1
you chose red!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option0
you chose blue!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option3
you chose yellow!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option4
>>> 
>>> 
============ RESTART: C:/Python/Python37-32/Day 7/colorchoice.py ============
0:blue
1:red
2:orange
3:yellow
4:quit
select a color option2
you chose orange!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option3
you chose yellow!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option1
you chose red!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option0
you chose blue!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option1
you chose red!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option2
you chose orange!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option3
you chose yellow!

0:blue
1:red
2:orange
3:yellow
4:quit
select a color option4
>>> n={'first':1,'second':2,'third':3,'five':5}
>>> n
{'first': 1, 'second': 2, 'third': 3, 'five': 5}
>>> print(sorted(n))
['first', 'five', 'second', 'third']
>>> print sorted(n,reverse=True))
SyntaxError: invalid syntax
>>> print(sorted(n,reverse=True))
['third', 'second', 'five', 'first']
>>> print(sorted(numbers.value()))
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    print(sorted(numbers.value()))
NameError: name 'numbers' is not defined
>>> print(sorted(n.value()))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(sorted(n.value()))
AttributeError: 'dict' object has no attribute 'value'
>>> print(sorted(n.values()))
[1, 2, 3, 5]
>>> print(sorted(n.values(),reverse=True))
[5, 3, 2, 1]
>>> print(sorted(n,keys=n.___getitem__))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print(sorted(n,keys=n.___getitem__))
AttributeError: 'dict' object has no attribute '___getitem__'
>>> print(sorted(n,keys=n.__getitem__))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print(sorted(n,keys=n.__getitem__))
TypeError: 'keys' is an invalid keyword argument for sort()
>>> print(sorted(n,key=n.__getitem__))
['first', 'second', 'third', 'five']
>>> ['first', 'second', 'third', 'five']print(sorted(n,key=n.__getitem__))
SyntaxError: invalid syntax
>>> print(sorted(n,key=n.__getitem__,reverse=True))
['five', 'third', 'second', 'first']
>>> 
========= RESTART: C:/Python/Python37-32/Day 7/exceptionhandling.py =========
Traceback (most recent call last):
  File "C:/Python/Python37-32/Day 7/exceptionhandling.py", line 6, in <module>
    print(kelvintofahreneit(273))
NameError: name 'kelvintofahreneit' is not defined
>>> 
>>> 
========= RESTART: C:/Python/Python37-32/Day 7/exceptionhandling.py =========
32.0
451.00399999999996
Colder than absolute zero
thank you
>>> 
============ RESTART: C:/Python/Python37-32/Day 7/dividebyzero.py ============
6.666666666666667
5.0
Division by zero is not defined
thank you
>>> 
