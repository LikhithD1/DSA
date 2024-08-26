def cycle(head):
  fast,slow = head,head
  while fast and fast.next:
    slow= slow.next
    fast=fast.next.next

    if slow==fast:
      return true
  return false
  
