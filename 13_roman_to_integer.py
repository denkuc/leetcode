class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        integer = 0
        for index, char in enumerate(s):
            increment = roman_to_int_map.get(char)
            next_increment = roman_to_int_map.get(s[index+1]) if index != len(s)-1 else 0
            if next_increment > increment:
                increment = -increment
            integer += increment

        return integer
