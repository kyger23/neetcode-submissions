class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = ''.join(sorted(word))
            seen.setdefault(key, []).append(word)
        return list(seen.values())
