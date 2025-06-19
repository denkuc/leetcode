import re


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit for group, digit in re.findall(r'((.)\2*)', s))
        return s

    def countAndSay(self, n: int) -> str:
        index = 0
        spelled = "1"

        while index+1 != n:
            spelled = self.__spellNumber(spelled)
            index += 1

        return spelled

    def __spellNumber(self, number_to_spell: str) -> str:
        spelled = ""
        count = 0
        previous = ""
        for index, digit in enumerate(number_to_spell):
            if index == 0 or digit == previous:
                count += 1
            else:
                spelled += str(count)
                spelled += previous
                count = 1
            previous = digit

        spelled += str(count)
        spelled += previous

        return spelled

assert Solution().countAndSay(1) == "1"
assert Solution().countAndSay(2) == "11"
assert Solution().countAndSay(3) == "21"
assert Solution().countAndSay(4) == "1211"
assert Solution().countAndSay(5) == "111221"
print(re.findall(r'((.)\2*)', "111221"))
