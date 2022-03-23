'''
STACK Method

1. In this method we will use stack LIFO concept through List.
2. We will itterate through every character present in the string if
   2.1 S[i] will be any of "{, [, (" them then we will append that character in the Stack (List / Array at the end).
   2.2 S[i] will be any of "}, ], )" them and the stack is empty then it will not eber a correct order as wont able to pop out so will return true.
   2.3 S[i] will be any of "}, ], )" them and the stack top (List / Array last index element) is it opposite sign (like for '(' --> Stack top is ')'. ) Sililarly for others.
3. After itteration we will check if stack is empty or not if it is menas we have valid Set else there is any element left states that we dont have valid pair for that.
'''

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            elif(stack==[] and i in ["}","]",")"]):
                return False
            else:
                if (i==")" and stack[-1]=="("):
                    del stack[-1]
                elif (i=="}" and stack[-1]=="{"):
                    del stack[-1]
                elif (i=="]" and stack[-1]=="["):
                    del stack[-1]
                else:
                    return False
        if (stack==[]):
            return True
        else:
            return False
          
'''
Time Complexity: O(N)
Space Cpmplexity: O(N)
'''
