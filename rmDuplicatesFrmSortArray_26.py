"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only
once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 
respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified
to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""

class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0

		i=j=0
		ans = 1

		while j < len(nums):
			while nums[j] <= nums[i]:
				if j == len(nums):
					return ans
				else:
					j+=1
			if j == i+1:
				i+=1;j+=1
			else:
				i+=1
				self.swap(nums,i,j)
				j+=1
			ans+=1

			print(nums)

		return ans

	def swap(self,List,a,b):
		tmp = List[a]
		List[a] = List[b]
		List[b] = tmp

if __name__ == "__main__":

	mysol = Solution()

	nums1 = [1,1,2]
	nums2 = [0,0,1,1,1,2,2,3,3,4]
	nums3 = [-48,-48,-44,-43,-43,-43,-40,-39,-39,-38,-37,-36,-36,-33,-31,-30,-30,-30,-29,-29,-28,-27,-27,-26,-26,-24,-23,-22,-21,-20,-20,-19,-19,-17,-17,-17,-15,-13,-13,-13,-12,-11,-11,-10,-10,-10,-8,-2,-1,-1,0,1,2,4,5,5,6,6,7,8,8,8,9,10,10,10,12,12,13,14,15,16,16,17,17,19,19,21,21,22,23,24,24,26,27,27,27,27,28,28,28,31,31,32,32,37,37,39,39,40,40,42,42,43,43,44,45,46,46,47,48,48,48,49,50]

	ans = mysol.removeDuplicates(nums3)
	print(ans)

