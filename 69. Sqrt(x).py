class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0

        while start * start <= x:
            if start * start < x:
                # print(start)
                start += 1
            elif start * start == x:
                return start
        return start - 1