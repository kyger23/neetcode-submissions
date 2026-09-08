class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
           return False
       seen = {}
       for item in s:
           seen[item] = seen.get(item, 0) + 1
       for item in t:
           if item not in seen or seen[item] == 0:
               return False
           seen[item] -= 1
       return True
