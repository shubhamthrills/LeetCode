class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        LengthOfString=len(s)
        LastOctate=LengthOfString%k
        if(LastOctate):
            s+=fill*(k-LastOctate)
        #NumberOfParts=LengthOfString//k
        res=[] 
        for i in range(0, LengthOfString, k):
            res.append(s[i:i+k])
        return (res)
        #import textwrap
        #return (textwrap.wrap(s, NumberOfParts))
