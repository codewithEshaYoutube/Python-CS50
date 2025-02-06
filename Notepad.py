class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for needle in haystack:
            return [needle]
        else:
            return -1
    haystack = "sadbutsad"
    needle = "sad"
    88. Merge Sorted Array