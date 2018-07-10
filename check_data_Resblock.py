# -*- coding: utf-8 -*-
# @Author: zhanglishi001
# @Date:   2018-07-09 15:07:55
# @Last Modified by:   zhanglishi001
# @Last Modified time: 2018-07-09 16:01:04

import os,sys
import xlrd,xlwt
import pdb

def checkResult(fileName,outFilePath):
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('resblock',cell_overwrite_ok = True)
    sheet.write(0, 0,"index")
    sheet.write(0,1,"resblock_id")
    sheet.write(0,2,'resblock_name')
    sheet.write(0,3,'resblock_id_query')
    sheet.write(0,4,'resblock_name_query')

    index = 0
    with open(fileName,'r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line_items = line.strip().split(',')
                if(line_items[3] == "0"):# or line_items[2] != line_items[-1]):
                    index = index+1
                    for id,item in enumerate(line_items):
                        sheet.write(index,id,item)

    with open(fileName,'r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line_items = line.strip().split(',')
                len_num = len(line_items)
                if(line_items[3] != "0" and line_items[2] != line_items[-1]):
                    index = index+1
                    for id,item in enumerate(line_items):
                        sheet.write(index,id,item)
    # 最后，将以上操作保存到指定的Excel文件中
    book.save(outFilePath)  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错

def testCode(fileName,outFilePath):
    checkResult(fileName,outFilePath)



def main():
    fileName = './checkresult.txt'
    outFilePath = r'./result_resblock.xls'
    testCode(fileName,outFilePath)
    print("check result is over!!!")


if __name__ == '__main__':
    main()