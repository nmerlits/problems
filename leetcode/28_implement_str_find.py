class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for ind, letter in enumerate(haystack):
            if letter == needle[0]:
                if haystack[ind:ind+len(needle)] == needle:
                    return ind            
        return -1