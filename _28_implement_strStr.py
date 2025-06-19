class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        else:
            str_str = 0
            index_needle = 0
            for index, char in enumerate(haystack):
                if char == needle[index_needle]:
                    index_needle += 1
                    if index_needle == len(needle):
                        break
                else:
                    index_needle = 0
                    str_str = index + 1

            return str_str if str_str != len(haystack) else -1


assert Solution().strStr("mississippi", "issip") == 4
assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("aaaaaaaaaaa", "baa") == -1
