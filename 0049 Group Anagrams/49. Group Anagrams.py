from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for i in strs:
            sorted_s = ''.join(sorted(i))
            anagram_map[sorted_s].append(i)

        return list(anagram_map.values())        