class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            a=arr.pop(0)
            if a in [n*2 for n in arr] :
                return True
            arr.append(a)
        return False