class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = Counter(s), Counter(t)
        return dict_s == dict_t