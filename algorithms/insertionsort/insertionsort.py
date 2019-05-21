#!/usr/bin/python

# ascending
def insertion_sort_asc(A):
	for i in range(1, len(A)):
		j = i
		while j > 0 and A[j-1] > A[j]:
			t = A[j]
			A[j] = A[j-1]
			A[j-1] = t
			j -= 1

# descending
def insertion_sort_desc(A):
	for i in range(1, len(A)):
		j = i
		while j > 0 and A[j-1] < A[j]:
			t = A[j]
			A[j] = A[j-1]
			A[j-1] = t
			j -= 1

# main()
if __name__ == "__main__":	
	A = [8, 3, 1, 6, 10, 2, 9, 5, 7, 4]
	insertion_sort_asc(A)
	print("Ascending: {}".format(A))
	insertion_sort_desc(A)
	print("Descending: {}".format(A))