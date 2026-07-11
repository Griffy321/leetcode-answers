class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen and n != 1:
            seen.add(n)
            n = sum(int(number) ** 2 for number in str(n))
        return n == 1