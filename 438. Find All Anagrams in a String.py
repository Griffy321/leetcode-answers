from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict

        hashMap = defaultdict(int)
        results = []
        pLen = len(p) # short one
        sLen = len(s) # long one

        for letter in p:
            hashMap[letter] += 1

        for i in range(sLen):
            if s[i] in hashMap:
                hashMap[s[i]] -= 1 # remove from the letter key if the value we're on is in the hashmap
            if i >= pLen and s[i - pLen] in hashMap: # if we've itterated over the legth of p and have been doing thing so the hashmap we will want to add values back to the hashmap to try and balance it 
                hashMap[s[i - pLen]] += 1
            if i >= pLen - 1 and all(v == 0 for v in hashMap.values()):
                start_index = i - pLen + 1
                results.append(start_index)
        return results