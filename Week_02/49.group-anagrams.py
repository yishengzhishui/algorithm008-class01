class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 排序
        # result = collections.defaultdict(list)
        #
        # for s in strs:
        #     key = tuple(sorted(s))
        #     result[key].append(s)
        #
        # return result.values()

        # 计数
        result = {}
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1

            key = tuple(count)
            result[key] = result.get(key, []) + [s]

        return result.values()
