class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp=[]
        for num in range(len(nums)):
            tmp.append(sum(nums))
            nums.pop(-1)
            print(tmp)
        tmp.reverse()
        return tmp