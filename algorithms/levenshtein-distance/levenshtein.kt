fun levenshtein(w1:String, w2:String): Int {
	val w1s: String = w1.toLowerCase()
	val w2s: String = w2.toLowerCase()
	val n1: Int = w1s.length + 1
	val n2: Int = w2s.length + 1
	val d = Array(n1, {IntArray(n2)})

	for (y in 1..n1-1) {
		for (x in 1..n2-1) {
			if (w1s[y-1] == w2s[x-1])	{ 
				d[y][x] = d[y-1][x-1]
			} else {
				d[y][x] = minOf(d[y-1][x-1], minOf(d[y-1][x], d[y][x-1])) + 1
			}
		}
	}

	return d[n1-1][n2-1]
}


fun main() {
	println(levenshtein("Roman", "Ramo"))
}