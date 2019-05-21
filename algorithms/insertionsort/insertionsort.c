/* build: gcc -Wall -ansi -o insertionsort insertionsort.c */

#include <stdio.h>

/* ascending */
void insertion_sort_asc(int A[], int n) {
	int i,j,t;
	for(i=1; i<n; i++) {
		j = i;
		while(j > 0 && A[j-1] > A[j]) {
			t = A[j];
			A[j] = A[j-1];
			A[j-1] = t;
			j -= 1;
		}
	}
}

/* descending */
void insertion_sort_desc(int A[], int n) {
	int i,j,t;
	for(i=1; i<n; i++) {
		j = i;
		while(j > 0 && A[j-1] < A[j]) {
			t = A[j];
			A[j] = A[j-1];
			A[j-1] = t;
			j -= 1;
		}
	}
}

void print_array(int A[], int n) {
	int i;
	printf("[");
	for(i=0; i<n; i++) {
		if(i == n-1) printf("%d", A[i]);
		else printf("%d, ", A[i]);
	}
	printf("]\n");
}

int main(int argc, char **argv) {
	int A[] = { 8, 3, 1, 6, 10, 2, 9, 5, 7, 4 };
	int n = sizeof(A) / sizeof(int);
	
	insertion_sort_asc(A, n);
	printf("Ascending: "); print_array(A, n);
	insertion_sort_desc(A, n);
	printf("Descending: "); print_array(A, n);
	
	return 0;
}