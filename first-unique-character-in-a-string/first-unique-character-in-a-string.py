class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = -1
        # (1) Iterate through the string
        ch2idx_map = {}
        seen_chars = set()
        for idx, ch in enumerate(s):
            if ch not in seen_chars:
                ch2idx_map[ch] = idx
                seen_chars.add(ch)
            else:
                # Safely delete the key
                ch2idx_map.pop(ch, None)
        # (2) Sort the values in the HashMap in ascending order
        sorted_items = sorted(ch2idx_map.items(), key=lambda item:item[1])
        
        if sorted_items:
            return sorted_items[0][1]

        return -1