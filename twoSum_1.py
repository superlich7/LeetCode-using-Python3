""" 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]

		use one pass hash method, only one loop
		if complement is a hash key, then return the results
		if not ,then add {nums[i]:i} into hash
		"""
		nums_dic = {}

		for i in range(len(nums)):
			complement = target - nums[i]
			if(complement in nums_dic):
				print("found two sum solution at position {} and {}".format(i,nums_dic[complement]))
				return i , nums_dic[complement]
			nums_dic[nums[i]] = i

		print("not found two sum solution")

if __name__ == "__main__":
	mySolution = Solution() 

	nums = [2,7,11,15]
	target = 9

	mySolution.twoSum(nums,target)
	
