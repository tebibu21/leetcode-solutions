class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Traverse the string from right to left
        for ch in reversed(s):
            value = roman[ch]
            if value < prev_value:
                total -= value   # subtract if smaller comes before larger (e.g., IV = 4)
            else:
                total += value
            prev_value = value

        return total


# --- quick tests ---
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),     # L(50) + V(5) + III(3)
        ("MCMXCIV", 1994)  # M(1000) + CM(900) + XC(90) + IV(4)
    ]

    for s, expected in tests:
        result = sol.romanToInt(s)
        print(f"{s} -> {result}  (expected {expected})")