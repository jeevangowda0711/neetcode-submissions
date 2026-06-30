class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict_s, dict_t = Counter(s), Counter(t)
        # return dict_s == dict_t
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for c in s:
            dict_s[c] += 1
        for c in t:
            dict_t[c] += 1
        return dict_s == dict_t