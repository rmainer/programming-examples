import java.util.Arrays;

public class Levenshtein {

	private static int levenshtein(String w1, String w2) {
		w1 = w1.toLowerCase();
		w2 = w2.toLowerCase();
		int n1 = w1.length() + 1;
		int n2 = w2.length() + 1;

		// arrays in Java are always initialized with zeros
		// see: https://docs.oracle.com/javase/specs/jls/se7/html/jls-4.html#jls-4.12.5
		int[][] d = new int[n1][n2];

		for(int y=0; y<n1; y++) d[y][0] = y;
		for(int x=0; x<n2; x++) d[0][x] = x;

		for(int y=1; y<n1; y++) {
			for(int x=1; x<n2; x++) {
				if(w1.charAt(y-1) == w2.charAt(x-1)) {
					d[y][x] = d[y-1][x-1];
				} else {
					d[y][x] = Math.min(d[y-1][x-1], Math.min(d[y-1][x], d[y][x-1])) + 1;
				}
			}
		}

		return d[n1-1][n2-1];
	}

	public static void main(String[] args) {
		System.out.println(levenshtein("Roman", "Ramon"));
	}

}