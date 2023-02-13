class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        i=1
        while True:
            if target -i in nums:
                return nums.index(target-i)+1
            if target<min(nums):
                return 0
            i+=1
            
        