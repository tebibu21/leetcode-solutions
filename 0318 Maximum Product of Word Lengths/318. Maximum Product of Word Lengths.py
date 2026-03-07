class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [len(word) for word in words]

        # Build bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks[i] = mask

        max_product = 0

        # Compare pairs
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product