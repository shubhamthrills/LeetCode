'''
**✔️ Sliding window Approch **

1. We use a dictionary to store the character as the key and the last appear index has been seen so far as value.
2. When we encounter a repeated character in our  window then we will update the one of the temporary pointer with that key's value present in dictonary.

**CASE 1**: If s[r] not in seen, we can keep increasing the window size and store in maxLength and put that key in our dictonary.

**CASE 2**: If s[r] in seen:

**CASE 2.1** : s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]]+1 (+1 because index starts from 0).

**CASE 2.2**: s[r] is not inside the current window, we can keep increase the window and update.

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,maxLength,seen = 0,0,{}
        for i in range(len(s)):
            if s[i] in seen and start <= seen[s[i]]:
                start = seen[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            seen[s[i]] = i
        return maxLength
      
      

'''
 Time Complexity: O(N)
 Space Complexity: O(N)
 
 
 Get in touch with me @ github.com/shubhamthrills
                       www.linkedin.com/in/shubhamsagar/
'''
