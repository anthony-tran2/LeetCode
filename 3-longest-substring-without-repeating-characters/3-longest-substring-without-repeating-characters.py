class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_index = maxLength = 0
        used_chars = {}
        
        for i in range(0, len(s)):
            if s[i] in used_chars and start_index <= used_chars[s[i]]:
                start_index = used_chars[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start_index + 1)

            used_chars[s[i]] = i
        return maxLength