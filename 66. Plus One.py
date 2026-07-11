class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strNum = ""
        for num in digits:
            strNum += str(num)
            
        number = int(strNum) + 1
        return [int(num) for num in str(number)]