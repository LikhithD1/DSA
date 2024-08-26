class ListNode:
    def __init__(self,value,next):
        self.value=value
        self.next=none
def merge(l1,l2):
    dummy=ListNode()
    curr=dummy
    
    while l1 and l2:
        if l1.val <l2.val:
            curr.next=l1
            l1=l1.next
            
        else:
            curr.next=l2
           l2=l2.next
    
        curr=curr.next
    if l1:
        curr.next=l1
    else:
        curr.next=l2
    return dummy.next
