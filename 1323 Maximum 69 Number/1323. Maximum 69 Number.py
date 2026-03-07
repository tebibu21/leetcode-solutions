class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert to string
        s = list(str(num))
        
        # Change the first '6' to '9'
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                break
        
        # Convert back to int
        return int("".join(s))