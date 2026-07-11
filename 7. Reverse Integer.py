class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            str = f"{x}"
            value = int(str[::-1])
        else:
            str = f"{x * -1}"
            value =  int(str[::-1]) * -1

        upper = 2147483647
        lower = -2147483648
        if value < lower or value > upper:
            return 0
        return value