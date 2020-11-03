class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        s = list()
        top = -1
        
        headAns = None
        ptr = headAns
        
        p = head
        while(p != None or top > -1):
            newnode = Node(p.val, None, None, None)
            if headAns == None:
                headAns = newnode
                ptr = newnode
            else:
                ptr.next = newnode
                newnode.prev = ptr
                ptr = newnode
                
            if p.child != None:
                if p.next != None:
                    s.append(p.next)
                    top += 1
                p = p.child
            elif p.next != None:
                p = p.next
            elif top > -1:
                p = s.pop(-1)
                top -= 1
            else:
                break
                
        return headAns