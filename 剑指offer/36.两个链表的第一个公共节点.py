'''输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示
是用其他方式显示的，保证传入数据是正确的）
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        stack1 = []
        stack2 = []

        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        common = None
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()                  
            if node1 != node2:
                break
            else:
                common = node1
        return common 


        
