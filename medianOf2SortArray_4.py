"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

class Solution:
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float

		use a mergeSort based method:
		merge 2 sorted list into one
		deal with the return considering the total num is odd or even
		"""
		length_tol = len(nums1)+len(nums2)
		length = length_tol//2+1
		j=k=ans=tmp=0

		for i in range(length):
			if(j>=len(nums1)):
				ans = nums2[k]
				k+=1
			elif(k>=len(nums2)):
				ans = nums1[j]
				j+=1
			elif(nums1[j]<nums2[k]):
				ans = nums1[j]
				j+=1
			else:
				ans = nums2[k]
				k+=1

			if i == length-2:
				tmp = ans

		if length_tol%2 == 0:
			return (ans+tmp)/2
		else:
			return ans


if __name__ == "__main__":
	mySolution = Solution()	

	nums1 = [1, 2]
	nums2 = [3 ,4]

	ans = mySolution.findMedianSortedArrays(nums1,nums2)
	print(ans)

