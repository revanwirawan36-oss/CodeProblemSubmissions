def reverse(llist):
    prev=None
    curr=llist
    
    while curr is not None:
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
        
    return prev
