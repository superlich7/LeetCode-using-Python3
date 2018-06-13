"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in
spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""

		if len(matrix) == 0:
			return []

		row = len(matrix)
		col = len(matrix[0])
		ans = []
		stride = 0

		while row > 0 and col > 0:
			if row >= 2 and col >= 2:
				for i in range(stride,stride+col):
					ans.append(matrix[stride][i]) 
				for i in range(stride+1,stride+row):
					ans.append(matrix[i][stride+col-1]) 
				for i in range(0,col-1):
					ans.append(matrix[stride+row-1][stride+col-2-i])
				for i in range(0,row-2):
					ans.append(matrix[stride+row-2-i][stride])
				row -= 2
				col -= 2
				stride += 1
			elif row == 1 and col == 1:
				ans.append(matrix[stride][stride])
				row -= 1
				col -= 1
			elif row == 1:
				for i in range(col):
					ans.append(matrix[stride][stride+i])
					row -= 1
			elif col == 1:
				for i in range(row):
					ans.append(matrix[stride+i][stride])
					col -= 1

		return ans
			
if __name__ == "__main__":
	mysol = Solution()

	mat0 = [
	[ 1, 2, 3, 4, 5 ],
	[ 4, 5, 6, 5, 6 ],
	[ 4, 5, 6, 5, 6 ],
	[ 4, 5, 6, 5, 6 ],
	[ 7, 8, 9, 1, 7 ]]

	mat1 = [[3,1,3]]
	mat2 = [[3],[1],[3]]
	mat3 = [[3]]

	ans = mysol.spiralOrder(mat0)
	print(ans)

