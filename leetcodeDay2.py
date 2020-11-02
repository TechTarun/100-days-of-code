class Solution:
    
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            ele = arr[i]
            j = i-1
            while(j >= 0 and arr[j] > ele):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = ele   
        
    def insertionSortList(self, head: ListNode) -> ListNode:
        arr = list()
        ptr = head
        while(ptr != None):
            arr.append(ptr.val)
            ptr = ptr.next
        
        self.insertionSort(arr)
        print(arr)
        
        ptr = head
        for i in range(len(arr)):
            ptr.val = arr[i]
            ptr = ptr.next
            
        return head