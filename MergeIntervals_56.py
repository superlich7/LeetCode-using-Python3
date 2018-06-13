"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		if len(intervals) == 0:
			return []

		ans = []

		intervals.sort(key=lambda x: x.start)

		for interval in intervals:
			if not ans or ans[-1].end < interval.start:
				ans.append(interval)
			else:
				ans[-1].end = max(ans[-1].end,interval.end)

		return ans