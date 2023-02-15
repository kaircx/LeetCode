class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tmp = 0
        for i in range(len(nums)):
            if tmp == sum(nums)-nums[0]:
                return i
            tmp +=nums.pop(0)
        return -1