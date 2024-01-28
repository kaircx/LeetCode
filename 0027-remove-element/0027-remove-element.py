class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        if len(nums)==0:
            return 0
        while True:
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
            if i>=len(nums):
                break
        return len(nums)
        
        