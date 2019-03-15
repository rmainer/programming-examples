#!/usr/bin/python

# run with: python -B -m pydoc -w pydoc-example.py

class Arithmetic:
	"""
	Aritmetic example class
	"""

	def __init__(self):
		"""
		Constructor, nothing to do
		"""
		pass

	def add(self, x, y):
		"""
		Add two numbers x and y
		
		:param x: first summand
		:param y: second summand
		:returns: sum of x and y
		"""
		return x + y


if __name__ == '__main__':
    a = Arithmetic()
    print(a.add(1, 2))