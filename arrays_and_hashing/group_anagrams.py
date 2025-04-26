from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #First I am going to play around with defaultdict to see how it works
        pass

    playing = defaultdict(list)
    playing['a'].append('b')
    playing['a'].append('c')
    print(playing)