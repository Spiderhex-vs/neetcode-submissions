class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s, l_t = len(s), len(t)
        if l_s != l_t:
            return False

        counter_s, counter_t = dict(), dict()

        for i in range(l_s):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        for c in counter_s:
            if counter_s[c] != counter_t.get(c, 0):
                return False
        return True