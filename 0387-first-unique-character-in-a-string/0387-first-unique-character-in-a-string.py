class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                isDupe = False
                for j in range(i+1, len(s)):
                    if s[i] == s[j]:
                        isDupe = True
                        break

                if not isDupe:
                    return i

            seen.add(s[i])

        return -1