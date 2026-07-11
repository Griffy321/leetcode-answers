class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        stringDict = {}
        for str in strs:
            stringDict[str] = len(str)
        shortest = min(stringDict.values())

        chop = []
        # print(shortest)
        for value in strs:
            chop.append(value[0:shortest])
        # print(f"Chopped values : {chop}")

        
        while len(set(chop)) > 1:
            index = 0
            for str in chop:
                chop[index] = str[0:shortest - 1]
                index += 1
                # print(str)
            shortest -= 1
        # print(set(chop))
        return chop[0]