class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1  
        for c in ransomNote:
            if c not in counter:
                return False
            else:
                if counter[c] > 1:
                    counter[c] -= 1
                else:
                    del counter[c]                      
        return True