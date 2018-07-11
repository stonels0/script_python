# -*- coding: utf-8 -*-
# @Author: stonels0
# @Date:   2018-07-10 20:06:45
# @Last Modified by:   stonels0
# @Last Modified time: 2018-07-11 10:06:08
import os,sys
import itertools	# 迭代器工具;
import pdb

def testFunc():
	for n in itertools.count(100,2):
		if 1000<n<1010:
			print(n)
		if n > 1010:
			break

	count = 0
	for c in itertools.cycle('AB'):	# 无限重复
		if count > 4:
			break
		print(c)
		count += 1
	for x in itertools.repeat("hello world", 5): # 重复生成 object,此处为5次;
		print(x)

def main():


if __name__ == '__main__':
	main()