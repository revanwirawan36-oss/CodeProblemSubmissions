def compare_lists(llist1, llist2):
    curr1=llist1
    curr2=llist2
    
    
    while(True):
        if curr1.data!=curr2.data:
            return 0
        if (curr1.next==None and curr2.next != None) or (curr2.next==None and curr1.next!= None):
            return 0
        if curr1.next==None and curr2.next==None: break
        curr1=curr1.next
        curr2=curr2.next
        
    return 1
