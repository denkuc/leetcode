class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(abs(x))
        inverted_string_x = string_x[::-1]
        inverted_x = -int(inverted_string_x) if x < 0 else int(inverted_string_x)
        if not -2 ** 31 < inverted_x < 2 ** 31:
            return 0

        return inverted_x

