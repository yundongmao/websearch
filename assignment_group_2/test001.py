import json
import re
import collections
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

collections.defaultdict(int)


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s = set(banned)
        m = collections.defaultdict(int)
        words = re.split(",| |\.|\!|;|\'|\?", paragraph)
        for word in words:
            m[word.lower()] += 1
        if "" in m:
            m.pop("")
        ll = sorted([(m[word], word) for word in m.keys()], reverse=True)
        for tup in ll:
            if tup[1] not in s:
                return tup[1]


a = Solution()
print a.mostCommonWord("Bob", [])
