from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        len_p = len(p)
        len_s = len(s)
        
        if len_s < len_p:
            return res
        
        p_count = Counter(p)
        window_count = Counter(s[:len_p])  # initial window
        
        # Check first window
        if window_count == p_count:
            res.append(0)
        
        # Slide the window
        for i in range(len_p, len_s):
            start_char = s[i - len_p]
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char]  # keep dicts comparable
            
            window_count[s[i]] += 1  # add new char
            
            if window_count == p_count:
                res.append(i - len_p + 1)
        
        return res