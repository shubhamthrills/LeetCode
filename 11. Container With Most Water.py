'''
1. Two Pointer Method

1. We will Set the one pointer at start and one at the end of the array.
2. Then we will calculate the minimum height because in a container we can fill till minimum height only.
3. the widh of the selection will be our difference of both the pointer.
4. then we will calculate the area and compare with max and if it is max then we aill update the max with bigger area.
5. Now we will move the smaller height value towards centre / towards other wall.
   -->Why we will move smaller wall only why not bigger one?? 
   Becasue  
   1. If we move bigger one and suppose we find more bigger wall but then also we cant fill above the lower wall value becasue it will flow out.
      so, the area of water will decrease because wall height is same but widh is srinked.
   2. If we have smaller height encounter then also since width is srinked and the wall also then definetly the area will be srinked.
   3. If same height wall found then the over all area will be low because wall height will be constant but width will be srinked.
   
   So. It is the best one to move smaller height wall for by passing  all the fails/ lower capacity cases.



1. Start with pointer start = 0 and pointer end = length-1
2. The max water is limited by the pointer with smaller height
3. While srinking the array or moving forward or backward, the width of the area decrease
4. If we move the pointer with higher height, we will never get a greater area, the max height will be at most the one of the pointer with smaller height.
5. So we need to move the pointer with smaller height to have a chance to get higher height at the next step.



2. Brute Force:

In this we will simply try to make all pair of combination and find the area and if it bigger then update the MaxArea variable.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointer
        # Time Complexity: O(N) Space Complexity: O(1)
        start,end,MaxArea=0,len(height)-1,0
        while(start<end):
            ContainerWidth = end - start
            ContainerHeight = 0
            if (height[start] > height[end]):
                ContainerHeight = height[end]
                end -= 1
            else:
                ContainerHeight = height[start]
                start += 1
            TempArea = ContainerWidth * ContainerHeight
            MaxArea = max(MaxArea,TempArea)
        return (MaxArea)
    
    
    ''' 
        # Time Complexity: O(N^2) Space Complexity: O(1)
        MaxArea=0
        for i in range (len(height)-1):
            for j in range (i+1,len(height)):
                ContainerWidth = j - i
                ContainerHeight = min(height[i],height[j])
                TempArea = ContainerWidth * ContainerHeight
                MaxArea = max(MaxArea,TempArea)
        return (MaxArea)
        '''
    
    
    '''
    1. Two Pointer Method:
        Time Complexity: O(N)
        Space Complexity: O(1)
    
    2. Brute Force Method:
        Time Complexity: O(N^2)
        Space Complexity: O(1)
    '''
