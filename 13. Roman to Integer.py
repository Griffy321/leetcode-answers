class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueDict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        }

        numbers = []
        # get raw numbers
        for val in s:
            numbers.append(valueDict[val])

        numsToSubtract = []
        numsToAdd = []
        counter = 1
        for currNumber in numbers:
            try:
                if currNumber >= numbers[counter]:
                    numsToAdd.append(currNumber)
                else:
                    numsToSubtract.append(currNumber)
            except Exception:
                numsToAdd.append(currNumber)
            counter += 1
        return (sum(numsToAdd) - sum(numsToSubtract))