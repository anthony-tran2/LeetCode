class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s):
            return True
        s_arr = list(s)
        counter = 0
        
        for char in t:
            if counter == len(s_arr):
                return True
            if char == s_arr[counter]:
                counter += 1
        if counter == len(s_arr):
            return True
        return False