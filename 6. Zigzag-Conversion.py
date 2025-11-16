class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        i = 0
        d = 1
        
        for w in s:
            rows[i].append(w)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d  

        ret = ""
        for i in range(numRows):
            ret += ''.join(rows[i])    

        return ret       
