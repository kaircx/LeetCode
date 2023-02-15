class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(a) for a in list(str(k+int("".join(map(str,num)))))]