class Solution:
    def countElements(self, nums: List[int]) -> int:
        MinumumNumber=min(nums)
        MaximumNumber=max(nums)
        res=0
        for i in nums:
            if(MinumumNumber < i < MaximumNumber):
                res+=1
        return (res)
