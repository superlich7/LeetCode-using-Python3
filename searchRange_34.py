"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of
a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if len(nums) == 0:
			return [-1,-1]

		lo = 0
		hi = len(nums)-1
		while lo < hi:
			mid = lo + (hi-lo)//2
			if nums[mid] >= target:
				hi = mid 
			elif nums[mid] < target:
				lo = mid + 1
		left = lo

		lo = 0
		hi = len(nums)-1
		while lo < hi:
			mid = lo + (hi-lo)//2
			if nums[mid] > target:
				hi = mid - 1
			elif nums[mid] <= target:
				lo = mid + 1
		right = hi if nums[hi]==target else hi-1

		return [left,right] if nums[left] == target else [-1,-1]

if __name__ == "__main__":

	mysol = Solution()
	nums = [5,7,7,8,8,10]
	nums = [0,1]

	ans = mysol.searchRange(nums,1)
	print(ans)
