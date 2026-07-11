class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        indexDict = {}
        counter = 0

        for letter in s:
            indexDict[counter] = ""
            for comparison in s[counter:]:
                if indexDict[counter].find(comparison) == -1:
                    indexDict[counter] = indexDict[counter] + comparison
                else:
                    break
            counter += 1

        return max([len(val) for val in indexDict.values()])