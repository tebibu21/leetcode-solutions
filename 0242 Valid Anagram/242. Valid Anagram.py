class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for i in t:
            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else:
                counter[i] -= 1
        if len(counter) == 0:        
            return True
        return False                   