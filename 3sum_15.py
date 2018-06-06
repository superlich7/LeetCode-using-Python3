"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""

		if nums == None or len(nums) < 3:
			return []
		
		ans = []
		nums.sort()

		for i in range(len(nums)-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			lo = i+1
			hi = len(nums)-1
			while(lo<hi):
				sums = nums[i] + nums[lo] + nums[hi]
				if sums < 0:
					lo+=1
				elif sums > 0:
					hi-=1
				else:
					ans.append([nums[i],nums[lo],nums[hi]])
					while lo<hi and nums[lo+1] == nums[lo]:
						lo+=1
					while lo<hi and nums[hi-1] == nums[hi]:
						hi-=1
					lo+=1
					hi-=1
		return ans

