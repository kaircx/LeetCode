class Solution:
    def countAndSay(self, n: int) -> str:
        def base(number):
            r=[]
            tmp=0
            for a in str(number):
                if tmp!=a:
                    r.append(str(1))
                    r.append(str(a))
                if tmp == a:
                    r[len(r)-2]=str(int(r[len(r)-2])+1)    
                tmp=a
            return "".join(r)
        ans=1
        for i in range(n-1):
            ans=base(ans)
        return str(ans)
            
        