class Solution:
    def isValid(self, s: str) -> bool:
        o = ""
        p = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in p.values():
                o += c
            elif c in p.keys():
                if len(o) == 0 or o[-1] != p.get(c):
                    return False
                o = o[:-1]

        return True if o == "" else False


assert Solution().isValid("()") is True
assert Solution().isValid("()[]{}") is True
assert Solution().isValid("(]") is False
assert Solution().isValid("([)]") is False
assert Solution().isValid("{[]}") is True
assert Solution().isValid("[([]])") is False
assert Solution().isValid("]") is False
