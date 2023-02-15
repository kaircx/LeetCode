class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        while len(nums)>=1:
            if target == nums.pop(0):
                return i
            if len(nums)<1:
                return -1
            if target == nums.pop(-1):
                return len(nums)+i+1
            i+=1
        return -1