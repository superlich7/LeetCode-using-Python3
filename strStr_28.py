"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question
to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""

class Solution:
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""

		if len(needle) == 0 :
			return 0
		if len(haystack) < len(needle):
			return -1
		flag = True

		for i in range(len(haystack)):
			if haystack[i] == needle[0]:
				flag = True
				if len(needle) == 1:
					return i
				for j in range(len(needle)-1):
					if i+1+j > len(haystack)-1:
						return -1
					if haystack[i+1+j] != needle[j+1]:
						flag = False
						break
				if j == len(needle)-2 and flag == True:
					return i

		return -1

if __name__ == "__main__":

	mysol = Solution()
	haystack = "hello"
	needle = "ll"

	ans = mysol.strStr(haystack,needle)
	print(ans)
