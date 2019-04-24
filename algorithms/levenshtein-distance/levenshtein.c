#include <ctype.h>
#include <stdio.h>
#include <string.h>

int min(int a, int b) {
	if(a < b) return a;
	else return b;
}

int levenshtein(char *w1, char *w2) {
	int n1 = strlen(w1) + 1;
	int n2 = strlen(w2) + 1;

	char s1[n1+1];
	char s2[n2+1];
	strncpy(s1, w1, n1);
	strncpy(s2, w2, n2);

	char *p1 = s1;
	char *p2 = s2;
	for(;*p1;++p1) *p1 = tolower(*p1);
	for(;*p2;++p2) *p2 = tolower(*p2);
	
	int d[n1][n2];
	memset(d, 0, sizeof(int) * n1 * n2);

	int x, y;
	for(y=1; y<n1; y++) d[y][0] = y;
	for(x=1; x<n2; x++) d[0][x] = x;

	for(y=1; y<n1; y++) {
		for(x=1; x<n2; x++) {
			if(s1[y-1] == s2[x-1]) {
				d[y][x] = d[y-1][x-1];
			} else {
				d[y][x] = min(d[y-1][x-1], min(d[y-1][x], d[y][x-1])) + 1;
			}
		}
	}

	return d[n1-1][n2-1];
}

int main(int argc, char **argv) {
	printf("%d\n", levenshtein("Roman", "Ramon"));
	return 0;
}
