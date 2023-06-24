class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }

        result=0
        previous_value=0

        for c in s:
            value=roman[c]
            if value >previous_value:
                result += value-2*previous_value

            else:
                result+= value
            
            previous_value=value
            
        return result