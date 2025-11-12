class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}        # map char -> last index where it appeared
        start = 0              # start index of current window (inclusive)
        max_len = 0

        for i, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= start:
                start = last_index[ch] + 1

            last_index[ch] = i
            curr_len = i - start + 1
            if curr_len > max_len:
                max_len = curr_len

        return max_len


# --- quick tests ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcabcbb", 3),   # "abc"
        ("bbbbb", 1),      # "b"
        ("pwwkew", 3),     # "wke"
        ("", 0),           # empty string
        (" ", 1),          # single space
        ("au", 2),
        ("dvdf", 3)        # "vdf"
    ]

    for s, expected in tests:
        result = sol.lengthOfLongestSubstring(s)
        print(f"'{s}' -> {result}  (expected {expected})")
