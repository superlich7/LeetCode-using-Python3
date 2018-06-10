"""
Merge two sorted linked lists and return it as a new list. The new list should be made
by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

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
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)

	l2 = ListNode(1)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)

	l = mysol.mergeTwoLists(l1,l2)
	while l != None:
		print(l.val)
		l = l.next
