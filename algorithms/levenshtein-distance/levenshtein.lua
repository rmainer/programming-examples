function levenshtein(w1, w2)
	w1 = w1:lower()
	w2 = w2:lower()
	n1 = w1:len() + 1
	n2 = w2:len() + 1

	d = {}
	for y=1,n1 do
		d[y] = {}
		for x=1,n2 do
			d[y][x] = 0
		end
	end
	for y=2,n1 do
		d[y][1] = y
	end
	for x=2,n2 do
		d[1][x] = x
	end

	for y=2,n1 do
		for x=2,n2 do
			if w1:sub(y-1,y-1) == w2:sub(x-1,x-1) then
				d[y][x] = d[y-1][x-1]
			else
				d[y][x] = math.min(d[y-1][x-1], d[y-1][x], d[y][x-1]) + 1
			end
		end
	end

	return d[n1][n2]
end


print(levenshtein("Roman", "Ramon"))