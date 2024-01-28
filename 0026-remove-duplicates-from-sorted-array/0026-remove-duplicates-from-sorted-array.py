class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=-101
        i=0
        while True:
            if k==nums[i]:
                k=nums.pop(i)
                i-=1
            else:
                k=nums[i]
            i+=1
            if i>len(nums)-1:
                break
        return i
        