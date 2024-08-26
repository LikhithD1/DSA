1.ITERATIVE 

class ListNode:
    def _init_(self, value, next):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None  
    current = head  
    
    while current:
        next_node = current.next  
        current.next = prev 
        prev = current 
        current = next_node 
    return prev  
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_list(head)

2.RECURVISE 

class ListNode:
    def _init_(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    if not head or not head.next:
        return head
      
    new_head = reverse_list(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head

head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_list(head)

