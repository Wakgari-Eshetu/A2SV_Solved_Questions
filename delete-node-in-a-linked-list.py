class ListNode:
    def __init__(self , x):
        self.val = x
        self.next = next

class Solution:
    def deleteNode(node):
        node.val = node.next.val
        node.next = node.next.next