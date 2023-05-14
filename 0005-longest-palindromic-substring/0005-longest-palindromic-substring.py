class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=s[0]
        if len(s)==1:
            return s
        def isPalindromic(s):
            for i in range(len(s)):
                if s[i]!=s[len(s)-1-i]:
                    return False
            # print("it is")
            return True
        for a in range(len(s)):
            tmp=s[a]
            index=len(s)
            while tmp in s[a+1:index]:
                index=s.rfind(tmp,a+1,index)
                # print("-",tmp,a,index,"-")
                # print(s[a:index+1])
                # print("------")
                if len(ans)<len(s[a:index+1]):
                    if isPalindromic(s[a:index+1]):
                        ans=s[a:index+1]
                else:
                    break
                        # print("answer is ",ans)
                # index-=1
        return ans
        
                    