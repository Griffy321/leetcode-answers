def findTheDifference(s: str, t: str) -> str:
    from collections import defaultdict
    sIntDict = defaultdict(int)

    for letter in s:
        sIntDict[letter] += 1
    print(sIntDict)
    
    for letter in t:
        if letter not in list(sIntDict.keys()):
            return letter
        else:
            sIntDict[letter] -= 1
        
    return sorted(sIntDict, key=sIntDict.__getitem__)[0]

s = "abcd"
t = "abcde"

s = "abb"
t = "aabb"

print(findTheDifference(s,t))