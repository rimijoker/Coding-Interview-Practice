def riverSizes(matrix):
	sizes = []
	seen = [[False for i in row] for row in matrix]
	
	def findSize(r, c):
		if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and not seen[r][c] and matrix[r][c]):
			return 0
		seen[r][c] = True
		return (1 + findSize(r+1, c) + findSize(r-1, c) + findSize(r, c-1) + findSize(r, c+1))
	
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			size = findSize(r, c)
			if size != 0 :
				sizes.append(size)
	return sizes
