class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        from collections import defaultdict
        s1Len = len(s1)
        s2Len = len(s2)
        hashMap = defaultdict(int)
        for character in s1:
            hashMap[character] += 1
        for index in range(s2Len):
            if s2[index] in hashMap:
                hashMap[s2[index]] -= 1
            if index >= s1Len and s2[index - s1Len] in hashMap:
                hashMap[s2[index - s1Len]] += 1
            if index >= s1Len - 1 and all(v == 0 for v in hashMap.values()):
                return True
        return False
