class Loops {
	public static void main(String [] args) {
		int i=0;

		// while
		while(i<5) {
			System.out.println(i);
			i++;
		}

			// for
			for(int j=0; j<5; j++) {
				System.out.println(j);
			}

			// break
			for(int j=0; j<5; j++) {
				System.out.println(j);
				if(j==3) break;
			}

		}
}