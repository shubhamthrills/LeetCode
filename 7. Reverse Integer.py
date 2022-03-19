'''
1. First we will determine the inputted number is positive or negative and store a corresponding unique place holder in a variable (flag).
2. If the number is negative then we will make it positive.
3. Break the integer into list of characters.
4. And will itterate till half of the list and in every itteration we will swap the i th element and len(x)-i-1 th element.
5. After swaping (Two Pointer swaping) we will convert the list to string then to integer so that if the number is starting with 0's then it will be removed.
   (Like 01 will be 1 or 001 will be 1)
6. Now we will check if the original number is negative or not using the flag variable and if it was negative then we will make it negative by multiplying it by (-1).
7. Now the last condition if the modified value go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 else wewill return the modified x.
'''

class Solution:
    def reverse(self, x: int) -> int:            
        flag= 'positive'
        if x<0:
            x *= -1
            flag='negative'
        x=list(str(x))
        for i in range(len(x)//2):
            x[i],x[len(x)-i-1]=x[len(x)-i-1],x[i]
        x=''.join(x)
        x=int(x)
        if flag=='negative':
            x *= -1
        if (-(2**31)-1 <= x <= 2**31):
            return (x)
        else:
            return (0)
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
