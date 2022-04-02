'''
✔️ Two Pointer Method

1. In this method we will take two pointer say start and end.
2. Initially start will poinnt to 0th Index and end will point to last index i.e., len(s)-1
3. we will traverse till mid of the string using while loop having condition start<=end (This will cover both the case of even or odd length string)
4. In each itterartion we will compare if both charater is same or not if same then we continue till find the 1st character which does not match that we need to remove by incrementing start and decrementing end. 
5. After encountring the different character we will form two string first without start pointing character(StringFirstCharRemoval) and other without the end pointing character(StringLastCharRemoval)
6. After that we will check is both string is palidrom or not and return the True or False.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while(start<=end):
            if(s[start] != s[end]):
                StringFirstCharRemoval=s[:start] + s[start+1:]
                StringLastCharRemoval=s[:end] + s[end+1:]
                return (StringFirstCharRemoval == StringFirstCharRemoval[::-1] or StringLastCharRemoval == StringLastCharRemoval[::-1])
            start +=1
            end -= 1
        return True
'''
Time Complexity: O(N)

# --------- Please UPVOTE the solution if you like the approach ---------

For any help or query related to coding problem reach me at
Linkedin:  https://www.linkedin.com/in/shubhamsagar/
                                            OR
Follow me on github for other leetcode solutions : https://github.com/shubhamthrills/
'''
