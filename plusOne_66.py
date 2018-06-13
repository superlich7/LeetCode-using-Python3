"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each
element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""

		if len(digits) == 0:
			return []

		if digits[-1] < 9:
			digits[-1] += 1
			return digits
		else:
			digits[-1] = 0
			carry = 1
			for i in range(len(digits)-1):
				if digits[-2-i] + carry == 10:
					digits[-2-i] = 0
				else:
					digits[-2-i] += carry
					return digits
			if digits[0] == 0:
				digits.insert(0,1)
			return digits

if __name__ == "__main__":
	mysol = Solution()

	digits0 = [1,2,3]
	digits1 = [4,3,2,1]
	digits2 = [1,1,9]
	digits3 = [9,9,9]

	ans = mysol.plusOne(digits0)
	print(ans)
	ans = mysol.plusOne(digits1)
	print(ans)
	ans = mysol.plusOne(digits2)
	print(ans)
	ans = mysol.plusOne(digits3)
	print(ans)

			
			
