class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split sentence into words
        if len(pattern) != len(words):  # If lengths don’t match, return False
            return False

        char_to_word = {}  # Mapping from pattern -> word
        word_to_char = {}  # Mapping from word -> pattern

        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False  # Mismatch in existing mapping
            if word in word_to_char and word_to_char[word] != char:
                return False  # Mismatch in reverse mapping

            char_to_word[char] = word
            word_to_char[word] = char

        return True  # Pattern matches the word structure


# Example Usage:
sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))  # True
print(sol.wordPattern("abba", "dog cat cat fish"))  # False
