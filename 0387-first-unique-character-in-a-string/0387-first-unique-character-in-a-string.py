# Time: O(n^2); Space: O(num_unique_chars)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Maintain a HashSet to keep track of the past characters
        seen = set()
        # Iterate through every character
        for i in range(len(s)):
            # Check if we've already seen the character
            if s[i] not in seen:
                isDupe = False
                # Check every subsequent character
                for j in range(i+1, len(s)):
                    # Found the character twice, exit checking
                    if s[i] == s[j]:
                        isDupe = True
                        break

                # Found a unique character
                if not isDupe:
                    return i # return index

            seen.add(s[i]) # Add the current character to the visited set

        return -1 # didn't find any unique character