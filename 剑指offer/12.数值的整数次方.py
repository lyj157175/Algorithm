'''给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0

输入
2,3
返回值
8.00000
'''

class Solution:
    def Power(self, base, exponent):
        return pow(base, exponent)
        
        