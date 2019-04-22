#!/usr/bin/python

def levenshtein(w1, w2):
	w1 = w1.lower()
	w2 = w2.lower()
	n1 = len(w1) + 1
	n2 = len(w2) + 1
	d = [[0 for x in range(n2)] for y in range(n1)]
	
	for y in range(0, n1):
		d[y][0] = y
	for x in range(0, n2):
		d[0][x] = x

	for y in range(1, n1):
		for x in range(1, n2):
			if w1[y-1] == w2[x-1]:
				d[y][x] = d[y-1][x-1]
			else:
				d[y][x] = min(d[y-1][x-1], d[y-1][x], d[y][x-1]) + 1
	
	return d[n1-1][n2-1]

print(levenshtein("Roman", "Ramon"))
