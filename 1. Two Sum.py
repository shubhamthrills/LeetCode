'''
✔️ Solution: HashMap/ Dictonary
We need to find 2 numbers a, b so that a + b = target.

We need a HashMap/Dictonary datastructure to store elements in the past, let name it dic.

The idea is that we iterate i as each element in nums, and store the value of "nums[i] - target"

Then we will re iterate in nums and check wether nums[i]+x==0, because we have already subtracted the target means now we need to check the sum of two elemt as zero(0).

So, If -nums[i] exists in dic hashmap or dictonary or not then we already found 2 index one is "i" and other index will be value part of the element present in hashmap/dictonary , so that a + b = 0,

We will then return both their indices.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range (len(nums)):
            dic[nums[i]-target]=i
        for i in range (len(nums)):
            if -nums[i] in dic:
                index=dic.get(-nums[i])
                if index != i:
                    return([i,index])
                  
'''
Time Complexity : O(N)
Space Complexity: O(N)
'''
