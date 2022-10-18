# Time: O(n); Space: O(26) ~ O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create {ch: freq} dictionary
        freq_map = collections.Counter(s)

        # Iterate through every character
        for idx, ch in enumerate(s):
            # Check for unique character
            if freq_map[ch] == 1:
                return idx

        return -1 # no unique character