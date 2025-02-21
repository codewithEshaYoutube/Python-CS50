
class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # Iterate from the end of the string
            value = roman_map[char]
            if value < prev_value:
                total -= value  # Subtract if a smaller numeral precedes a larger one
            else:
                total += value
            prev_value = value

        return total

# Example Usage
sol = Solution()
print(sol.roman_to_int("XIV"))  # Output: 14
print(sol.roman_to_int("MCMXCIV"))  # Output: 1994




