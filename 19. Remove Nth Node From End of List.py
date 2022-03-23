'''
Two Pointer Method

1. We will have two pointer which will itterate over the linked list say fast and slow both initalized with head means pointing to the first node.
2. Now we will move the fast pointer to the number specified i.e, if we need to remove the last 2nd node then our fast node must be at last node and slow node 
   must be just before deleting node and if we observe there the difference between both pointer will be of that N node.
   So, Idea is to move the fast pointer N times ahead than slow and then after move both pointer by one till fast reaches last node.
   
3. Once fast pointer reaches last node we will update the next filed of the node at which slow is pointing.
4. After hat we will free up the space of that deleted node bu making it reference to None to avoid dangling pointer.
5. Then we will return the head pointer.

For eg. let the list be 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, and n = 4.

1. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
   ^slow               ^fast
   |<--gap of n nodes-->|
 
 => Now traverse till fast reaches end
 
 2. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
                        ^slow               ^fast
                        |<--gap of n nodes-->|
						
'slow' is at (n+1)th node from end.
So just delete nth node from end by assigning slow -> next as slow -> next -> next (which would remove nth node from end of list).

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        LengthOfList = 0
        fast = slow = head
        for i in range (n):
            fast = fast.next
        if not fast:
            return head.next
        else:
            while(fast.next):
                fast = fast.next
                slow = slow.next
            DeletedNodePointer = slow.next
            slow.next = slow.next.next
            DeletedNodePointer.next = None #Removing dangling pointer
            return (head)
        
'''
Time Cpmplexity : O(N)
Space Complexity: O(1)
'''


'''
# --------- Please UPVOTE the solution if you like the approach ---------

Get in touch with me at linkedin:  https://www.linkedin.com/in/shubhamsagar/
Follow me on github for other leetcode solutions : https://github.com/shubhamthrills/
'''
        
