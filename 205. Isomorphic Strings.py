def isIsomorphic(s: str, t: str) -> bool:
    from collections import defaultdict
    sDict = defaultdict(list)
    tDict = defaultdict(list)

    for index in range(len(s)):
        sDict[s[index]].append(index)

    for index in range(len(t)):
        tDict[t[index]].append(index)

    print(sDict, tDict)

    sValues = [value for value in sDict.values()]
    tValues = [value for value in tDict.values()]
    print(sValues, tValues)
    if sValues == tValues:
        return True
    else:
        return False

# s = "egg"
# t = "add"

# s = "f11"
# t = "b23"

# s = "paper"
# t = "title"

s = "bbbaaaba"
t = "aaabbbba"

print(isIsomorphic(s, t))