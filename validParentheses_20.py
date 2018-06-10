"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		if s == None :
			return True

		dit = {'(':3, ')':6, '[':4, ']':8, '{':5, '}':10, }#use a dict to represent parentheses
		#left  parenttheses key's value is 3,4,5
		#right parenttheses key's value is 6,8,10 aims to be twice of matchable left parentheses
		stack = []

		for i in range(len(s)):
			if dit[s[i]] <= 5:
				stack.append(s[i])
			elif dit[s[i]] >5 and len(stack) > 0:
				if(dit[stack.pop()] != dit[s[i]]/2):
					return False
			elif dit[s[i]] >5 and len(stack) == 0:
				return False

		return True if len(stack) == 0 else False

if __name__ == "__main__":

	mysol = Solution()
	s1 = "()"
	s2 = "()[]{}"
	s3 = "(]"
	s4 = "([)]"
	s5 = "{[]}"
	s6 = ""
	s7 = "{"
	s8 = "]"

	ans = mysol.isValid(s1)
	ans = mysol.isValid(s2)
	ans = mysol.isValid(s3)
	ans = mysol.isValid(s4)
	ans = mysol.isValid(s5)
	ans = mysol.isValid(s8)
	print(ans)
