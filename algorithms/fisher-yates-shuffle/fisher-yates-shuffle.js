function fisher_yates_shuffle(a) {
	var j, t;
	for(let i=a.length-1; i>0; i--) {
		j = Math.floor(Math.random() * (i+1));
		t = a[i];
		a[i] = a[j];
		a[j] = t;
	}
	return a;
}

var A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(fisher_yates_shuffle(A));