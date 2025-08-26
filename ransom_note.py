def can_construct(ransomNote: str, magazine: str) -> bool:
    letter_counts = {}
    for letter in magazine:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in ransomNote:
        if letter_counts.get(letter, 0) == 0:
            return False
        letter_counts[letter] -= 1

    return True