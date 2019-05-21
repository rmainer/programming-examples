import java.util.Arrays;

class InsertionSort {

	// ascending
	private static void insertion_sort_asc(int [] A) {
		int i,j,t;
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
	private static void insertion_sort_desc(int [] A) {
		int i,j,t;
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

	public static void main(String[] args) {
		int [] A = {8, 3, 1, 6, 10, 2, 9, 5, 7, 4};
		insertion_sort_asc(A);
		System.out.println("Ascending: " + Arrays.toString(A));
		insertion_sort_desc(A);
		System.out.println("Descending: " + Arrays.toString(A));
	}

}