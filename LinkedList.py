from typing import Optional

import LinkedList

'''class ListNode:
    def __init__(self, val):
        # self.next = None
        # self.prev = None'''
'''
    def add_to_end(node_to_add):
        node_to_add.next = tail
        node_to_add.prev = tail.prev
        tail.prev.next = node_to_add
        tail.prev = node_to_add

    def remove_from_end(self):
        if head.next == tail:
            return

        node_to_remove = tail.prev
        node_to_remove.prev.next = tail
        tail.prev = node_to_remove.prev

    def add_to_start(node_to_add):
        node_to_add.prev = head
        node_to_add.next = head.next
        head.next.prev = node_to_add
        head.next = node_to_add

    def remove_from_start(self):
        if head.next == tail:
            return
        node_to_remove = head.next
        node_to_remove.next.prev = head
        head.next = node_to_remove.next

    def get_middle(head):
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next

        for _ in range(length // 2):
            head = head.next

        return head.val

    def get_middleTwoPointers(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val
'''

'''    head = ListNode(None)
    tail = ListNode(None)
    head.next = tail
    tail.prev = head'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or not head.next:
            return head

        slow = head
        fast = head.next

        while fast:
            if slow.val == fast.val:
                slow.next = slow.next.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next

        return head

    def reverse_list(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # first, make sure we don't lose the next node
            curr.next = prev  # reverse the direction of the pointer
            prev = curr  # set the current node to prev for the next node
            curr = next_node  # move on

        return prev

    def swapPairs(self, head: ListNode) -> ListNode:
        # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head

        dummy = head.next  # Step 5
        prev = None  # Initialize for step 3
        while head and head.next:
            if prev:
                prev.next = head.next  # Step 4
            prev = head  # Step 3

            next_node = head.next.next  # Step 2
            head.next.next = head  # Step 1

            head.next = next_node  # Step 6
            head = next_node  # Move to next pair (Step 3)

        return dummy

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        middle_node = self.middleNode(head)
        middle_node = self.reverse_list(middle_node)
        fast = middle_node
        max_sum = 0

        while fast:
            max_sum = max(fast.val + slow.val, max_sum)
            fast = fast.next
            slow = slow.next

        return max_sum

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return None

        slow, fast = head, head
        stop = False

        def recurseAndReverse(fast, left, right):
            nonlocal slow, stop

            # base case. Don't proceed any further
            if right == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            fast = fast.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if left > 1:
                slow = slow.next

            # Recurse with m and n reduced.
            recurseAndReverse(fast, left - 1, right - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if slow == right or fast.next == slow:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                slow.val, fast.val = fast.val, slow.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                slow = slow.next

        recurseAndReverse(fast, left, right)

        return head




one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
head_dup = one

print(Solution().reverseBetween(head_dup, 3, 5))

'''
list_node = ListNode(1)
node_to_add = 2
list_node.add_to_end()
node_to_add = 3
list_node.add_to_end()

print(list_node)'''
