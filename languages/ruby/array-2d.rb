# initialize 2d array with zeros
a = Array.new(3) { Array.new(6, 0) }

# print array
puts a.map { |x| x.join(' ') }
