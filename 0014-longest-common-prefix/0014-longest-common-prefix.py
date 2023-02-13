class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=[strs[0]]
        for i in range(len(strs)-1):
            answer=[]
            for m,n in zip(list(strs[i]),list(strs[i+1])):
                if m==n:
                    answer.append(m)
                else:
                    break
            strs[i+1]=answer
        return "".join(answer)
        