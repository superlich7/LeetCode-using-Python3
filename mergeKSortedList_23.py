"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its
complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""

		if len(lists) == 0 or lists == None:
			return None
		lo = 0
		hi = len(lists)-1

		return self.mergeKListsIndex(lists,lo,hi)

	def mergeKListsIndex(self,lists,lo,hi):
		if lo == hi:
			return lists[lo]

		mid = lo + (hi-lo)//2

		l1 = self.mergeKListsIndex(lists,lo,mid)
		l2 = self.mergeKListsIndex(lists,mid+1,hi)

		return self.merge2Lists(l1,l2)

	def merge2Lists(self,l1, l2):
		dummy = ListNode(0)
		tmp = dummy

		while l1 != None or l2 != None:
			if l2 == None:
				tmp.next = l1
				tmp = tmp.next
				l1 = l1.next
			elif l1 == None:
				tmp.next = l2
				tmp = tmp.next
				l2 = l2.next
			elif l1.val <= l2.val:
				tmp.next = l1
				tmp = tmp.next
				l1 = l1.next
			elif l1.val > l2.val:
				tmp.next = l2
				tmp = tmp.next
				l2 = l2.next

		return dummy.next

if __name__ == "__main__":

	mysol = Solution()
	
	l1 = ListNode(1)
	l1.next = ListNode(4)
	l1.next.next = ListNode(5)

	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)

	l3 = ListNode(2)
	l3.next = ListNode(6)
	
	lists = [l1,l2,l3]
	l = mysol.mergeKLists(lists)
	while l != None:
		print(l.val)
		l = l.next
