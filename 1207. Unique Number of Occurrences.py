from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        numOccurances = defaultdict(int)

        for number in arr:
            numOccurances[number] += 1

        occurances = [occurance for occurance in numOccurances.values()]
        if len(occurances) == len(set(occurances)):
            return True
        return False