'''
✔️ Two Pointer Swap Method

In this method we will take two pointer say start and end.
Initially start will poinnt to 0th Index and end will point to last index i.e., len(s)-1
we will traverse till mid of the string using while loop having condition start<end (This will cover both the case of even or odd length string)
In each itterartion we will swap the start and end pointing value.
And increment the start pointer and decrement the end pointer, in other word we are srinking the string after swapping the current character.
For Exapmple we have string s: ['h', 'e', 'l', 'l' , 'o']

0=>['h', 'e', 'l', 'l' , 'o']
     ^                    ^
     |                    |
   start                 end

At this point we will swap and increment start and decrement end

1=>  ['o', 'e', 'l', 'l' , 'h']
            ^         ^
            |         |
          start       end

2=>  ['o', 'l', 'l', 'e' , 'h']
                 ^
                 |  
            start & end
			
So the above string is reversed in INPLACE way without any extra space.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start,end = 0,len(s)-1
        while(start<end):
            s[start],s[end] =s[end], s[start]
            start += 1
            end -= 1    
            
'''            
Complexity:

Time Complexity: O(N)
Space Complexity: O(1)

# --------- Please UPVOTE the solution if you like the approach ---------

For any help or query related to coding problem reach me at
Linkedin:  https://www.linkedin.com/in/shubhamsagar/
                                            OR
Follow me on github for other leetcode solutions : https://github.com/shubhamthrills/
'''
