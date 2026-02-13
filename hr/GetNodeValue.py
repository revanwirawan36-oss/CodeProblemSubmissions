def getNode(llist, positionFromTail):
    prev=None
    curr=llist
    
    while curr is not None:
        nextNode=curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
        
    curr=prev
    for _ in range(positionFromTail):
        curr=curr.next
    return (curr.data)
