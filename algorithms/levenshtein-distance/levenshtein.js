function levenshtein(w1 ,w2) {
	var w1 = w1.toLowerCase();
	var w2 = w2.toLowerCase();
	var n1 = w1.length + 1;
	var n2 = w2.length + 1;
	var d = Array(n1).fill(0).map(_ => Array(n2).fill(0));

	for(let y=1; y<n1; y++) d[y][0] = y;
	for(let x=1; x<n2; x++) d[0][x] = x;

	for(let y=1; y<n1; y++) {
		for(let x=1; x<n2; x++) {
			if(w1[y-1] == w2[x-1]) {
				d[y][x] = d[y-1][x-1];
			} else {
				d[y][x] = Math.min(d[y-1][x-1], d[y-1][x], d[y][x-1]) + 1;
			}
		}
	}

	return d[n1-1][n2-1];
}

console.log(levenshtein("Roman", "Ramon"));