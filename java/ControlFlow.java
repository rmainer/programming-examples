// control flow examples

public class ControlFlow {
	
	public static void main(String [] args) {
		
		int a = 1;
		
		// ternary operator
		boolean b = (a == 1) ? true : false;

		// if-statement
		if(a < 0) {
			System.out.println("minor");
		}
		else if(a == 0) {
			System.out.println("zero");
		}
		else {
			System.out.println("major");
		}
		
		// switch-statement
    int i=2;
        
		switch(i){
			case 0:
				System.out.println("i is zero");
				break;
			case 1:
				System.out.println("i is one");
				break;
			case 2:
				System.out.println("i is two");
				break;
			case 3:
				System.out.println("i is three");
				break;
			default:
				System.out.println("i is something other");
        }
    } 		
}