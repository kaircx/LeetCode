class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            a=0
            for j,n in enumerate(needle):
                if n==haystack[i+j]:
                    a+=1
                else:
                    break
            if a == len(needle):
                return i
        return -1