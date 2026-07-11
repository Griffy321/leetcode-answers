class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        dict = defaultdict(int)

        for letter in s:
            dict[letter] += 1
        
        if min(dict.values()) != 1:
            return -1
        else:
            filtered = [key for key, val in dict.items() if val == 1]
            return s.index(filtered[0])