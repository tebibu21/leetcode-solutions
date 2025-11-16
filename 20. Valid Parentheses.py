class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop top element if stack not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if top element matches the required opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)

        # In the end, stack must be empty
        return len(stack) == 0