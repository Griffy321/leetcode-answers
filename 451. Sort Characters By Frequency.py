class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict

        letterFrq = defaultdict(int)
        results = ""

        for letter in s:
            letterFrq[letter] += 1

        while letterFrq is not None:
            try:
                key = max(letterFrq, key=letterFrq.get)
            except Exception:
                return results
            val = letterFrq[key]
            results += key * val
            letterFrq.pop(key)