// ascending
function insertion_sort_asc(A) {
	var i,j,t;
	for(i = 0; i < A.length; i++) {
		j = i;
		while(j > 0 && A[j-1] > A[j]) {
			t = A[j];
			A[j] = A[j-1];
			A[j-1] = t;
			j--;
		}
	}
}

// descending
function insertion_sort_desc(A) {
	var i,j,t;
	for(i = 0; i < A.length; i++) {
		j = i;
		while(j > 0 && A[j-1] < A[j]) {
			t = A[j];
			A[j] = A[j-1];
			A[j-1] = t;
			j--;
		}
	}
}

var A = [8, 3, 1, 6, 10, 2, 9, 5, 7, 4];
insertion_sort_asc(A);
console.log("Ascending: " + A);
insertion_sort_desc(A);
console.log("Descending: " + A);