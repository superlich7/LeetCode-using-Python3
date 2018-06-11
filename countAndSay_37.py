"""
The count-and-say sequence is the sequence of integers with the first five terms as
following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
"""

class Solution:
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""

		if n == 0:
			return None
		elif n == 1:
			return '1'

		tmp = 2
		str_old = str_new = '11'

		while tmp < n:
			str_old = '11' if tmp == 2 else str_new
			str_new = self.countAndSayRer(str_old)
			tmp+=1

		return str_new

	def countAndSayRer(self,str_old):
		str_new = ''
		count = 1

		for i in range(len(str_old)-1):
			if str_old[i] == str_old[i+1]:
				count+=1
			else:
				str_new = str_new + str(count) + str_old[i]
				count = 1
		
		if count == 1:
			return str_new + '1' + str_old[i+1]
		else :
			return str_new + str(count) + str_old[i+1]


if __name__ == '__main__':
	mysol = Solution()

	ans = mysol.countAndSay(9)
	print(ans)
