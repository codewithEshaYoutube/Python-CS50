def count_unique_letters(s: str) -> int:
    # Convert the string to lowercase and remove non-alphabetic characters
    s = ''.join(filter(str.isalpha, s.lower()))

    # Use a set to find unique letters
    unique_letters = set(s)
