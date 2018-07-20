# -*- coding: utf-8 -*-
# @Author: zhanglishi001
# @Date:   2018-07-18 22:05:07
# @Last Modified by:   zhanglishi001
# @Last Modified time: 2018-07-20 16:38:40
import os,sys
import pdb

import logging
logging.basicConfig(filename='log1.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)

def is_even(x):
    return x&1 != 0
def testcode():
    

    while True:
        option = input("input a digit:")
        if option.isdigit():
            print("hehe",option)
            logging.info('option correct')
        else:
            logging.error("Must input a digit!")


def main():
    pdb.set_trace()
    testcode()

if __name__ == '__main__':
    main()