class Solution:
    def romanToInt(self, s: str) -> int:
        FinalInteger=0
        temp=0
        RomanTable={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        #s=s[::-1]
        for i in reversed(s):
            if RomanTable[i]>=temp:
                FinalInteger=FinalInteger+RomanTable[i]
            else:
                FinalInteger=FinalInteger-RomanTable[i]
            temp=RomanTable[i]
        return FinalInteger
