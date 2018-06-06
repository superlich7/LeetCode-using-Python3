"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		signed = 0 if x >= 0 else 1
		ans = 0
		x = abs(x)
		while x//10 > 0:
			ans = ans*10 + x%10
			x//=10
		ans = ans*10 + x
		
		ans = ans if signed == 0 else -1*ans
		ans = 0 if ans > pow(2,31)-1 or ans < -1*pow(2,31) else ans

		return ans 

if __name__ == "__main__":

	mysol = Solution()
	test = 123 #-123 123456789987 -1*pow(2,31)
	res = mysol.reverse(test)
	print(res)
