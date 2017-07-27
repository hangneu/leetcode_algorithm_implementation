class Solution(object):
    def strStr(self, source, target):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if target[j] != source[i+j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1
