def levenshtein(w1, w2)
	w1 = w1.downcase
	w2 = w2.downcase
	n1 = w1.length
	n2 = w2.length
	d = Array.new(n1+1) { Array.new(n2+1, 0) }

	for y in 1..n1
		d[y][0] = y
	end
	for x in 1..n2
		d[0][x] = x
	end
	
	for y in 1..n1
		for x in 1..n2
			if w1[y-1] == w2[x-1]
				d[y][x] = d[y-1][x-1]
			else
				d[y][x] = [d[y-1][x-1], d[y-1][x], d[y][x-1]].min + 1
			end
		end
	end

	d[n1][n2]
end

puts levenshtein("Roman", "Ramon")