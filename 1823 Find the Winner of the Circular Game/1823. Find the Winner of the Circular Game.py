class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # start with one person, winner is at position 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1 