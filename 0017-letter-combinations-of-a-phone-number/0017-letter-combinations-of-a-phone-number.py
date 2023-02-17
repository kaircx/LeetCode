class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def match(a,b):
            d=[[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
            r=[]
            if a==0:
                return d[int(b)-1]
            for m in a:
                for n in d[int(b)-1]:
                    r.append(m+n)  
            print("r",r)
            return r
        tmp=0
        if digits=="":
            return ""
        for s in digits:
            print(tmp,s)
            tmp=match(tmp,s)
        return tmp
        
        