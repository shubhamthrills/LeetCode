'''
In this method 
1. We will find the lowest length string and save its length to a variable along with that string into a variable named "LongestPrefix".
   Because Longest commmon prefix among all the string passed will not greater that the minimum length it would be either smaller or equal to the length of the 
   smallest length of the string present.
2. After finding the miniumum length string we will itterate through every elemnt presennt in the list
3. In each itteration we will Slice the string from 0th index to the minimum length value and will compare every character and onces it not matched then then we will 
   update the MinLength & LongestPrefix variable.
4. we will keep updating the values till last element and at the end we will have the LongestPrefix that we will return. 
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        MinLength,LongestPrefix=len(strs[0]),""
        if len(strs)<1:
            return (LongestPrefix)
        elif(len(strs)==1):
            return (strs[0])
        else:
            for i in range (len(strs)):
                if (MinLength >= len(strs[i])):
                    MinLength = len(strs[i])
                    LongestPrefix = strs[i]
                    
            for i in range (len(strs)):
                temp=strs[i]
                temp=temp[:MinLength+1]
                for j in range (MinLength):
                    if (temp[j] != LongestPrefix[j]):
                        MinLength = j
                        LongestPrefix = LongestPrefix[:j]
                        break
            return (LongestPrefix)
          
          
'''
Time Complexity: O(N^2)
Space Complexity: O(1)
'''
