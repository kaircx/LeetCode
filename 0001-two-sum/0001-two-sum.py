class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = []
        a=[]
        for i in range(len(nums)):
            tmp.append(nums.pop(0))
            if target-tmp[i] in nums:
                a.append(i)
                a.append(nums.index(target-tmp[i])+i+1)
                return a
        
            