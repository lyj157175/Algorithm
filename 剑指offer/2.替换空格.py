'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的
字符串为We%20Are%20Happy。

输入
"We Are Happy"
返回值
"We%20Are%20Happy"
'''

class Solution:

    def replaceSpace(self, s):
        return s.replace(' ', '%20')
           