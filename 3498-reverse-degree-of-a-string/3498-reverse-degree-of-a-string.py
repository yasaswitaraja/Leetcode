class Solution:
    def reverseDegree(self, s: str) -> int:
        x=0
        for i in range(len(s)):
            x+= (i+1)*(122-ord(s[i])+1)
        return x
            
        