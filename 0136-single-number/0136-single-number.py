class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ref={}
        for num in nums:
            if num in ref:
                ref[num]+=1
            else:
                ref[num]=1
        return list(ref.keys())[list(ref.values()).index(min(list(ref.values())))]
        