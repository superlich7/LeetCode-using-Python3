"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""

class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int

		use only one loop n with hash
		with i grows,if no duplicate char in s[i], then hash it and compute longest
		else if meet a duplicate at s[i],then re-compute start indice and re-hash it
		"""
		start = 0
		longest = 0
		dit = {}

		for i in range(len(s)):
			if s[i] in dit:
				start = max(start,dit[s[i]]+1)
			longest = max(longest,i-start+1)
			dit[s[i]] = i
		return longest
				
if __name__ == "__main__":
	mySolution = Solution()	

	s1 = "abcabcbb"
	s2 = "bbbbb"
	s3 = "pwwkew"
	ans = mySolution.lengthOfLongestSubstring(s3)
	print(ans)
