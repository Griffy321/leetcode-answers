def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import defaultdict
    intDict = defaultdict(int)

    for letter in magazine:
        intDict[letter] += 1

    print(intDict)

    for letter in ransomNote:
        if letter in list(intDict.keys()):
            intDict[letter] -= 1
            if intDict[letter] < 0:
                return False
        else:
            return False
    return True

# ransomNote = "a"
# magazine = "b"

# ransomNote = "aa"
# magazine = "ab"

ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))