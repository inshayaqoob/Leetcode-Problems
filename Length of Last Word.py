class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        found_word = False  # Flag to check if we've encountered the first non-space character

        # Reverse the string and iterate through it
        for i in s[::-1]:
            if i == " " and not found_word:
                continue  # Skip leading spaces
            elif i == " " and found_word:
                break  # Break when we encounter a space after the last word
            else:
                found_word = True  # Mark that we've encountered the first non-space character
                count += 1  # Increment the count for characters in the last word

        return count
