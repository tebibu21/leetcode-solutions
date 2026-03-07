class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Map letters to rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lower_word = word.lower()
            # Determine which row the first letter is in
            if lower_word[0] in row1:
                row = row1
            elif lower_word[0] in row2:
                row = row2
            else:
                row = row3
            
            # Check if all letters are in the same row
            if all(char in row for char in lower_word):
                result.append(word)
        
        return result