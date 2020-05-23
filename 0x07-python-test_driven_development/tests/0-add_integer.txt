======================
TEST CASES FOR TASK 0
======================

>>> add_integer = __import__('0-add_integer').add_integer

>>> print(add_integer(1, 2))
3

>>> print(add_integer(100, -2))
98

>>> print(add_integer(2))
100

>>> print(add_integer(100.3, -2))
98

>>> print(add_integer(100, -2.9999))
98

>>> print(add_integer(--1))
99

add_integer()
Traceback (most recent call last):
	  ...
add_integer() missing 1 required positional argument: 'a'

>>> add_integer(float('inf'))
Traceback (most recent call last):
	  ...
OverflowError: cannot convert float infinity to integer

>>> add_integer(float('NaN'))
Traceback (most recent call last):
	  ...
ValueError: cannot convert float NaN to integer

>>> add_integer(--2++)
Traceback (most recent call last):
	  ...
SyntaxError: invalid syntax

>>> add_integer(var)
Traceback (most recent call last):
	  ...
NameError: name 'var' is not defined

>>> try:
...     print(add_integer(4, "School"))
... except Exception as e:
...     print(e)
b must be an integer

>>> try:
...     print(add_integer(None))
... except Exception as e:
...     print(e)
a must be an integer

>>> try:
...	print(add_integer(3, None))
... except Exception as e:
... 	print(e)
b must be an integer

>>> try:
...     print(add_integer("Holbrton", "School"))
... except Exception as e:
...     print(e)
a must be an integer

>>> try:
...     print(add_integer([2, 4, 6]))
... except Exception as e:
...     print(e)
a must be an integer

>>> try:
...     print(add_integer("a"))
... except Exception as e:
...     print(e)
a must be an integer

>>> try:
...	print(add_integer(True, False))
... except Exception as e:
... 	print(e)
a must be an integer
