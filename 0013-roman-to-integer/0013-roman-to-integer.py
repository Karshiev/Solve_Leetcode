class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        prev_value = 0

        # iterate dictionary from rigth to left
        for last_char in s[::-1]:
            current_value = roman_values[last_char]

            # if the previous value is greater than previous value (from right to left), substract it from  total 
            if prev_value > current_value:
                num -= current_value
            else:
                num += current_value
            
            prev_value = current_value

        return num



        