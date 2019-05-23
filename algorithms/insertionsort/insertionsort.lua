-- ascending
function insertion_sort_asc(A)
	local i, j
	for i = 2, #A do
		j = i
		while j > 1 and A[j-1] > A[j] do
			A[j-1], A[j] = A[j], A[j-1]
			j = j - 1
		end
	end
end

-- descending
function insertion_sort_desc(A)
	local i, j
	for i = 2, #A do
		j = i
		while j > 1 and A[j-1] < A[j] do
			A[j-1], A[j] = A[j], A[j-1]
			j = j - 1
		end
	end
end


-- main
A = { 8, 3, 1, 6, 10, 2, 9, 5, 7, 4 }
print("Original:   [" .. table.concat(A, ", ") .. "]")
insertion_sort_asc(A)
print("Ascending:  [" .. table.concat(A, ", ") .. "]")
insertion_sort_desc(A)
print("Descending: [" .. table.concat(A, ", ") .. "]")