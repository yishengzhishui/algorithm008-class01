import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # ls = list(str.strip())  # 去掉空格
        # if not ls: return 0
        # sign = -1 if ls[0] == '-' else 1
        #
        # if ls[0] in ['-', '+']: del ls[0]
        #
        # ret, i = 0, 0
        # while i < len(ls) and ls[i].isdigit():
        #     ret = ret * 10 + (ord(ls[i]) - ord('0'))
        #     i += 1
        #
        # return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

        # 正则表达式
        # ^：匹配字符串开头
        # [\+\-]：代表一个+字符或-字符
        # ?：前面一个字符可有可无
        # \d：一个数字
        # +：前面一个字符的一个或多个

        str = str.strip()  # 清除多余的空格
        num_re = re.compile('^[\+\-]?\d+')  # 设置正则规则
        num = num_re.findall(str)  # 查找匹配的内容
        result = int(*num)  # 由于返回的是个列表，解包并且转换成整数
        return max(-2 ** 31, min(result, 2 ** 31 - 1))  # 返回值
