class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ref=[]
        for num in nums:
            if num in ref:
                ref.pop(ref.index(num))
            else:
                ref.append(num)
        return ref[0]
        