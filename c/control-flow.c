#include <stdio.h>

int main(int argc, char **argv) {
	int a = 0;
	
	// if-statement
	if (a < 0) { 
		printf("minor");
	} else if(a == 0) {
		printf("zero");
	} else {
		printf("major")
	}
	
	// switch-statement
	char b = 'x';
	switch (someChar) {
		case 'a': printf('a'); break;
		case 'x': printf('x'); break;
		case 'y':
		case 'z': printf('y or z'); break;
		default: printf('default');
	}
	
	return 0;
}