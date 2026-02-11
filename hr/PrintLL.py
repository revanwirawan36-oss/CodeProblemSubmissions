def printLinkedList(head):
    curr=head
    
    while True:
        print(curr.data)
        if curr.next==None: break
        curr=curr.next
