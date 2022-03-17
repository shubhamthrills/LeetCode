'''
1. We observe that a palindrome mirrors around its center. 
2. Therefore, a palindrome can be expanded from its center toward both the sides.
3. When there is even length palindrome hen there would be two centre and for odd length palindrome there will be 1 centre
   for this reason we will call out helper function (ExpandfromCentre) considering both one by one.
4. ExpandfromCentre funnction is just comparing its left and right till it matches or till end of string.
5. ExpandfromCentre function will return the length of that perticular palindrome around that current element. 
6. After getting the length with the help of current index we will update the start and end variable.
7. and at last we will return the sliced string.
'''

def ExpandfromCentre(s,i,j):
        while(i>=0 and j<len(s) and s[i]==s[j]):
            i-=1
            j+=1
        return (j-i-1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start,end=0,0
        for i in range (len(s)):
            len1=ExpandfromCentre(s,i,i+1)
            len2=ExpandfromCentre(s,i,i)
            leng=max(len1,len2)
            if (end-start < leng):
                start=i-((leng-1)//2)
                end=i+(leng//2)
        return (s[start:end+1])        
      
      
      
'''
Time Complexity: O(N)
Space Complexity: O(1)

 Get in touch with me @ github.com/shubhamthrills
                       www.linkedin.com/in/shubhamsagar/
'''
