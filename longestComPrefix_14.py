"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
	def commonStr(self,str1,str2):
		"""
		:type str1,str2: str
		:rtype : str
		"""
		ans = ""
		i = 0

		while 1:
			if i == len(str1):
				return str1
			elif i == len(str2):
				return str2
			elif str1[i] == str2[i]:
				ans = ans + str1[i]
				i += 1
			else:
				return ans

	def longestCommonPrefixDiv(self, strs, start, end):
		"""
		:type strs:  List[str]
		:type start: int
		:type end:   int
		:rtype: str
		"""
		if start==end:
			return strs[start]

		mid = start + (end-start)//2
		pref1 = self.longestCommonPrefixDiv(strs,start,mid)
		pref2 = self.longestCommonPrefixDiv(strs,mid+1,end)

		return self.commonStr(pref1, pref2)

	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""

		if strs == None or len(strs) == 0:
			return ""

		return self.longestCommonPrefixDiv(strs,0,len(strs)-1)

if __name__ == "__main__":
	mysol = Solution()

	string1 = ["flower","flow","flight"]
	string2 = ["dog","racecar","car"]

	#result = mysol.longestCommonPrefix(string1)
	print(mysol.longestCommonPrefix(string2))

