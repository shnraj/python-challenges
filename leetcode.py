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


class LLRandomNodeSolution(object):

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


###

# 109. Convert Sorted List to Binary Search Tree

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

###

import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTree(self):
        print_arr = []
        pos = 0
        print_arr.append(self)
        while pos < len(print_arr):
            if print_arr[pos].left:
                print_arr.append(print_arr[pos].left)
            if print_arr[pos].right:
                print_arr.append(print_arr[pos].right)
            pos += 1
        for node in print_arr:
            print node.val


class LLToTreeSolution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Convert linked list to array
        arr = [head.val]
        while head.next is not None:
            arr.append(head.next.val)
            head = head.next

        # Function that converts list of sorted ints to binary tree
        def treeFromList(numList):
            if len(numList) == 0:
                return None
            elif len(numList) == 1:
                return TreeNode(numList[0])
            else:
                half = int(math.ceil(float(len(numList))/2)) - 1
                node = TreeNode(numList[half])
                node.left = treeFromList(numList[:half])
                node.right = treeFromList(numList[half+1:])
            return node

        return treeFromList(arr).printTree()

###

# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

###


def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        highest_int = 0
        start = 0
        x = 0
        seen = set()
        while x < len(s):
            if s[x] in seen:
                highest_int = max(len(seen), highest_int)
                seen = set()
                start += 1
                x = start
            else:
                seen.add(s[x])
                x += 1
        print max(len(seen), highest_int)


###

# 164. Maximum Gap

# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

###


def maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    highest_diff = 0
    nums.sort() # Use radix or bucket sort
    if len(nums) < 2: return 0
    for x in range(1, len(nums)):
        highest_diff = max(highest_diff, nums[x] - nums[x-1])
    return highest_diff


###

# 94. Binary Tree Inorder Traversal

# Given a binary tree, return the inorder traversal of its nodes' values.

# Recursive solution is trivial, what is the iterative solution?

###

def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


###

# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

###

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    total = 0
    for num in range(max(height), 0, -1):
        row = [i for i, x in enumerate(height) if x == num]
        if len(row) > 2:
            total += count(row)
        for v in row:
            height[v] = height[v] - 1
    print total


def count(row):
    count = 0
    for i, x in enumerate(row[1:]):
        y = x - row[i] - 1
        count += y
    return count


###

# 8. String to Integer (atoi)

# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

###

INT_MAX = 2147483647
INT_MIN = -2147483648


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    number = 0
    negative = False
    if not str:
        return 0
    else:
        nums = ''
        str = str.strip()
        if str[0] == '-':
            negative = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        for ch in str:
            if ch.isdigit():
                nums += ch
            else:
                break
        for i, num in enumerate(nums):
            number += (ord(num) - ord('0')) * 10**(len(nums) - 1 - i)
        if negative:
            number = number * -1
        if number > INT_MAX:
            return INT_MAX
        if number < INT_MIN:
            return INT_MIN
    return number

###

# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

###


class Sol(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        if word and board:
            starts = []
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] == word[0]:
                        starts.append(Coor(x, y))

            for start in starts:
                if self.test_start(start, word[1:], [start]):
                    return True
        return False

    def test_start(self, start_coor, word, seen):
        if word:
            for ch in word:
                spots = self.get_adjacent_spots(start_coor)
                result = False
                for spot in spots:
                    if ch == self.board[spot.x][spot.y] and not spot.found(seen):
                        new_seen = seen[:]
                        new_seen.append(spot)
                        result = result or self.test_start(spot, word[1:], new_seen)
                return result
        else:
            return True

    def get_adjacent_spots(self, coor):
        # Returns list of coordinates
        directions = [Coor(0, 1), Coor(1, 0), Coor(-1, 0), Coor(0, -1)]
        spots = []
        for dir in directions:
            new_coor = coor.add(dir)
            if new_coor.x >= 0 and new_coor.y >= 0 and new_coor.x < len(self.board) and new_coor.y < len(self.board[0]):
                spots.append(new_coor)
        return spots


class Coor():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_coor):
        return Coor(self.x + other_coor.x, self.y + other_coor.y)

    def found(self, arr_of_coor):
        for coor in arr_of_coor:
            if self.x == coor.x and self.y == coor.y:
                return True
        return False


if __name__ == '__main__':
    # 137. Single Number II
    #nums = [9, 2, 2, 2, 5, 5, 5]
    #sol1(nums)

    #sol2(nums)
    #sol3(nums)

    ## 382. Linked List Random Node
    #h = LLNode(1, LLNode(2, LLNode(3)))
    #sol = LLRandomNodeSolution(h)
    #sol.getRandom()

    ## 109. Convert Sorted List to Binary Search Tree
    #h = ListNode(1, ListNode(2, ListNode(4, ListNode(6, ListNode(7, ListNode(9))))))
    #h2 = ListNode(6, ListNode(7, ListNode(9)))
    #sol = LLToTreeSolution()
    #sol.sortedListToBST(h)

    ## 3. Longest Substring Without Repeating Characters
    #lengthOfLongestSubstring("abcabcbb")
    #lengthOfLongestSubstring("bbbb")
    #lengthOfLongestSubstring("pwwkew")
    #lengthOfLongestSubstring("c")
    #lengthOfLongestSubstring("")
    #lengthOfLongestSubstring("dvdf")
    #lengthOfLongestSubstring("abcadef")

    ## 164. Maximum Gap
    #maximumGap([1, 4, 7, 3, 2])
    #maximumGap([1000, 4, 7, 3, 2])
    #maximumGap([1, 1, 1])
    #maximumGap([1])

    # 42. Trapping Rain Water
    #trap([0,1,0,2,1,0,1,3,2,1,2,1])

    # 8. String to Integer (atoi)
    #myAtoi('  -1234 ab')
    #myAtoi('')
    #myAtoi('+-2')
    #myAtoi('+1')
    #myAtoi('2147483690')

    # 79. Word Search
    #x = Sol()
    #print x.exist(["ABCE", "SFCS", "ADEE"], "ABCCED")  # True
    #print x.exist(["ABCE", "SFCS", "ADEE"], "ABZ")  # False
    #print x.exist(["ABCE", "SFCS", "ADEE"], "ABCB")  # False
    #print x.exist(["ABCE", "SFCS", "ADEE"], "")  # False
    #print x.exist([""], "ABCCED")  # False
    #print x.exist(["b", "a", "b"], "bbabab")  # False
    #print x.exist(["CAA", "AAA", "BCD"], "AAB")  # True
    #print x.exist(["ABCE", "SFES", "ADEE"], "ABCEFSADEESE")  # True
