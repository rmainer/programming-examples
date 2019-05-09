#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int levenshtein(string w1, string w2) {
	transform(w1.begin(), w1.end(), w1.begin(), ::tolower);
	transform(w2.begin(), w2.end(), w2.begin(), ::tolower);
	int n1 = w1.length() + 1;
	int n2 = w2.length() + 1;
	int d[n1][n2];

	for(int y=0; y<n1; y++) {
		for(int x=0; x<n2; x++) {
			d[y][x] = 0;
		}
	}
	for(int y=1; y<n1; y++) d[y][0] = y;
	for(int x=1; x<n2; x++) d[0][x] = x;

	for(int y=1; y<n1; y++) {
		for(int x=1; x<n2; x++) {
			if(w1.at(y-1) == w2.at(x-1)) d[y][x] = d[y-1][x-1];
			else d[y][x] = min(d[y-1][x-1], min(d[y-1][x], d[y][x-1])) + 1;
		}
	}

	return d[n1-1][n2-1];
}

int main() {
	cout << levenshtein("Roman", "Ramo") << "\n";
	return 0;
}