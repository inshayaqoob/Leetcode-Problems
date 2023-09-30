class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Find the shortest string in the list.
        min_str = min(strs, key=len)

        # Loop through the characters in the shortest string.
        for i, char in enumerate(min_str):
            for string in strs:
                if string[i] != char:
                    return min_str[:i]  # Return the common prefix found so far.

        return min_str  # All strings are the same up to the length of the shortest one
