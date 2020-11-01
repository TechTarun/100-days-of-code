class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head == None:
            return 0
        """First method with O(n)/O(n)"""
        # ele = list()
#         ptr = head
#         while(ptr != None):
#             ele.append(ptr.val)
#             ptr = ptr.next
#         ele.reverse()
        
#         result = 0
#         for i in range(len(ele)):
#             result += (ele[i] * math.pow(2,i))
#         return int(result)

        """Second method with O(n)/O(1)"""
        result = 0
        ptr = head
        while(ptr != None):
            result = result << 1
            result += ptr.val
            ptr = ptr.next
        return result