def titleToNumber(columnTitle: str) -> int:
    
    answer = 0
    position = 0

    for letter in reversed(columnTitle):
        digit = ord(letter) - 64 # returns the unicode number for the letter, subtracting 64 keeps it in the standard 26 letter alphabet
        answer += digit * 26 ** position
        position += 1
    
    return answer

# columnTitle = "A"
# columnTitle = "AB"
columnTitle = "ZY"

print(titleToNumber(columnTitle))