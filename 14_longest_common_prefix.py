from typing import List


class Solution:
    def longestCommonPrefixMy(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix

        first_str = strs[0]
        for char in first_str:
            if not self.__starts_with_true(prefix + char, strs[1:]):
                return prefix

            prefix += char

        return prefix

    def __starts_with_true(self, prefix, strs) -> bool:
        for str_ in strs:
            if not str_.startswith(prefix):
                return False

        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for str_ in strs[1:]:
            while str_.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
