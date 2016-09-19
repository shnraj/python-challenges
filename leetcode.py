###

# 137. Single Number II
# Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

###

def sol1(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    for n, c in counts.iteritems():
        if c != 3:
            print n


def sol2(nums):
    nums_set = set(nums)
    for n in nums_set:
        if nums.count(n) != 3:
            print n


def sol3(nums):
    sorted_nums = sorted(nums)
    count = 0
    prev_n = sorted_nums[0]
    for num in sorted_nums:
        if num == prev_n:
            count += 1
        else:
            if count != 3:
                print prev_n
            count = 1
        prev_n = num
    print prev_n


###

# 382. Linked List Random Node
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Follow up:
# What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

###

from random import randint


class LLNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null,
        so it contains at least one node.
        :type head: ListNode
        """
        # Naive solution
        self.head = head
        self.arr = []
        self.arr.append(head.val)
        while head.next is not None:
            self.arr.append(head.next.val)
            head = head.next

        # Using Reservoir Sampling
        # http://www.geeksforgeeks.org/select-a-random-node-from-a-singly-linked-list/

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        print self.arr[randint(0, len(self.arr) - 1)]

if __name__ == '__main__':
    # 137. Single Number II
    nums = [9, 2, 2, 2, 5, 5, 5]
    sol1(nums)
    sol2(nums)
    sol3(nums)

    # 382. Linked List Random Node
    h = LLNode(1, LLNode(2, LLNode(3)))
    sol = Solution(h)
    sol.getRandom()

