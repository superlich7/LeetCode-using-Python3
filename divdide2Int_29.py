"""
Given two integers dividend and divisor, divide two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your
function returns 2^31 − 1 when the division result overflows.
"""

class Solution:
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""

		if 0 == dividend:
			return 0
		if dividend == -2147483648 and divisor == 1:
			return -2147483648

		signed = 1 if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
		ans = 0
		dividend = abs(dividend)
		divisor  = abs(divisor)

		while divisor <= dividend:
			tmp ,shift = divisor, 1
			while (tmp<<1) <= dividend:
				tmp <<= 1
				shift <<= 1
			dividend -= tmp
			ans += shift

		ans = min(ans,2147483647)
		return int(ans*signed)

if __name__ == "__main__":

	mysol = Solution()

	dividend = -2147483648
	divisor  = -1

	ans = mysol.divide(dividend,divisor)
	print(ans)

