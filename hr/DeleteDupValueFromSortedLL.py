def removeDuplicates(llist):
    curr=llist
    
    newNode=SinglyLinkedListNode(curr.data)
    
    head=newNode
    tail=newNode
    
    while True:
        prevVal=curr.data
        
        curr=curr.next
        if curr is None: break
        if curr.data!=prevVal:
            newNode=SinglyLinkedListNode(curr.data)
        else:
            continue
        tail.next=newNode
        tail=newNode
    return head
