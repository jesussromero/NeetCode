from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        helper_dict = {}
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            if key not in helper_dict:
                helper_dict[key] = []
            helper_dict[key].append(word)
            
        return list(helper_dict.values())