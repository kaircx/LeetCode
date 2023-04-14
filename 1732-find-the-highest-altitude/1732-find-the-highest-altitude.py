class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[0]
        for i,g in enumerate(gain):
            ans.append(ans[i]+g)
            print(ans)
        return max(ans)