# -*- coding: utf-8 -*-
# @Author: zhanglishi001
# @Date:   2018-07-10 10:58:45
# @Last Modified by:   zhanglishi001
# @Last Modified time: 2018-07-10 11:51:56
import os,sys
import xlrd,xlwt
import os
import pdb

def loadMap(filename):
    dict_map = {}
    workbook1 = xlrd.open_workbook(filename)
    resblockInfo = workbook1.sheet_by_name('sheet1')
    
    for id in range(1,resblockInfo.nrows):
        row_item = resblockInfo.row_values(id)
        key = row_item[4]
        value = row_item[3]
        dict_map[key] = value
    return dict_map

def query_data(inFileName1,inFileName2,outFilePath):
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('resblock_modify',cell_overwrite_ok = True)
    sheet.write(0, 0,"index")
    sheet.write(0,1,"resblock_id")
    sheet.write(0,2,'resblock_name')
    sheet.write(0,3,'resblock_id_query')
    sheet.write(0,4,'resblock_name_query')
    index = 0

    workbook2 = xlrd.open_workbook(inFileName2)
    dict_map = loadMap(inFileName1)

    checkBlockInfo = workbook2.sheet_by_name('resblock')
    # print(checkBlockInfo.name,checkBlockInfo.nrows,checkBlockInfo.ncols)

    for id in range(1,checkBlockInfo.nrows):
        row_item = checkBlockInfo.row_values(id)
        if row_item[3] == '0':
            name_query = row_item[2]
            resblock_id = dict_map.get(name_query,'0')
            if resblock_id != '0':
                row_item[3] = resblock_id # 替换查找ID;
                row_item[4] = row_item[2] # 替换为 楼盘名称;
        # 重新写入xls文件中;
        index = index + 1
        for id,item in enumerate(row_item):
            sheet.write(index,id,item)

    book.save(outFilePath)

def main():
    inFileName1 = './大连楼盘列表.xlsx'
    inFileName2 = './result_resblock.xls'
    outFilePath = './resblock_modify.xls'
    query_data(inFileName1,inFileName2,outFilePath)

if __name__ == '__main__':
    main()