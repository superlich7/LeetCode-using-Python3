"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative
integer.

Since the return type is an integer, the decimal digits are truncated and only the
integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution:
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x<= 0:
			return 0
		elif x == 1:
			return 1

		lo = 1
		hi = x
		while lo < hi:
			mid = lo + (hi-lo)//2
			if mid*mid == x:
				return mid
			elif mid*mid > x:
				hi = mid - 1
			else:
				lo = mid + 1

		return int(lo-1) if lo*lo > x else int(lo)

if __name__ == "__main__":
	mysol = Solution()

	x0 = 4
	x1 = 8
	x2 = 1
	x3 = 2
	x4 = pow(2,31)-1

	ans = mysol.mySqrt(x0)
	print(ans)
	ans = mysol.mySqrt(x1)
	print(ans)
	ans = mysol.mySqrt(x2)
	print(ans)
	ans = mysol.mySqrt(x3)
	print(ans)
	ans = mysol.mySqrt(x4)
	print(ans)
