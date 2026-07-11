class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        comparison = ""
        for val in reversed(x):
            comparison += val
        return (x == comparison)