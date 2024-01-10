class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=[[]for _ in range(numRows)]
        paper=[]
        t=numRows
        flag=False

        for i in range(len(s)):
            paper.append(t)
            if t!=1 and flag==False:
                t-=1
            elif t<numRows:
                t+=1
                flag=True
            elif t==numRows and flag==True:
                flag=False
                t-=1
            else:
                return s
        for p,s_x in zip(paper,s):
            ans[numRows-p].append(s_x)
        ans= [item for sublist in ans for item in sublist]
        return ''.join(str(item) for item in ans)
                
                
                
                
        
            
        