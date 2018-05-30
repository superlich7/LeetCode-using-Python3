"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		carry = 0
		l3 = ListNode(0)
		tmp1 = l1
		tmp2 = l2
		tmp3 = l3

		while tmp1 != None or tmp2 != None:
			if tmp1 != None:
				val1 = tmp1.val #use node.val only if node is not None
			else:
				val1 = 0

			if tmp2 != None:
				val2 = tmp2.val #use node.val only if node is not None
			else:
				val2 = 0
				
			val3 = val1 + val2 + carry #sum up with carry
			if val3 >= 10:
				val3 = val3 - 10
				carry =1
			else:
				carry = 0
				
			tmp3.next = ListNode(val3)
			tmp3 = tmp3.next
			
			if tmp1 != None:
				tmp1 = tmp1.next
			if tmp2 != None:
				tmp2 = tmp2.next

		if carry == 1:
			tmp3.next = ListNode(1) #if there is a carry after loop

		return l3.next #l3.val = 0 ,l3.next is the beginning of the result

if __name__ == "__main__":
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	mysol = Solution()
	l3 = mysol.addTwoNumbers(l1,l2)
	while l3 != None:
		print(l3.val)
		l3 = l3.next
