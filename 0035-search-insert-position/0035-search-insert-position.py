class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target >max(nums):
            return len(nums)
        for i,n in enumerate(nums):
            if target <=n:
                return i
            
        