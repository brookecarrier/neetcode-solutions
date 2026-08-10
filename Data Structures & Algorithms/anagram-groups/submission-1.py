class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for string in strs:
            # key is sorted chars
            key = ''.join(sorted(string))
            d[key].append(string)

        return list(d.values())


        