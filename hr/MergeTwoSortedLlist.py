def mergeLists(head1, head2):
    curr1=head1
    curr2=head2
    
    minimum=min(head2.data, head1.data)
    
    if minimum==head1.data:
        minimum=head1
    else:
        minimum=head2
        
    head=None
    tail=None
    curr=minimum
    newNode= SinglyLinkedListNode(0)
    
    '''
    we checked the node itself if it's exist, not if the .next exist
    because in the last traversal, the node would get updated to a None pointer
    '''
    while(curr1 is not None or curr2 is not None):
        if curr1 is not None and (curr2 is None or curr1.data<=curr2.data):
            val=curr1.data
            curr1=curr1.next
        else:
            val=curr2.data
            curr2=curr2.next
        newNode=SinglyLinkedListNode(val)
        
        '''
        1. mengganti tail.next akan mengganti semua alias untuk tail .next
        2. head hanya akan terganti sekali, ketika tail dan head merupakan satu alias, setelah head terganti, kita ganti tailnya dengan node yang lain, sehingga tidak satu alias no more
        ''' 
        
        if head==None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
   
    return head
