def lengthOfLoop(self, head):
    if(head is None):
        return

    slow=fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            count=1
            temp=slow.next
            while(temp != slow):
                count+=1
                temp=temp.next
                return count
    else:
        return 0