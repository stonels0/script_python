# -*- coding: utf-8 -*-
# @Author: zhanglishi001
# @Date:   2018-07-10 18:35:00
# @Last Modified by:   zhanglishi001
# @Last Modified time: 2018-07-10 19:55:25

import os,sys
import xlrd,xlwt
import pdb

def read_excel(filename,tableName):
	workBook = xlrd.open_workbook(filename)
	sheet1 = workBook.sheet_by_name(tableName)
	# print(sheet1.name,sheet1.nrows,sheet1.ncols)
	data = []
	for id in range(1,sheet1.nrows):
		data.append(sheet1.row_values(id))
	return data

def refresh_data_resblock(src_fileName,dst_fileName):
	file_dir = os.path.dirname(dst_fileName)
	if not os.path.exists(file_dir):
		os.makedirs(file_dir)

	excel_data = read_excel(src_fileName,'待刷')
	result = []
	sql_strline = "update `dl_org_resblock` set "
	for id,item in enumerate(excel_data):
		resblock_id_old = item[1]
		resblock_id_new = item[4]
		resblock_name_old = item[2]
		resblock_name_new = item[5]
		sql_res = sql_strline + "resblock_id="+resblock_id_new+",resblock_name='"+resblock_name_new+"' where resblock_id="+resblock_id_old+";"
		result.append(sql_res)
	with open(dst_fileName,'w',encoding='utf-8') as f:
		f.writelines('\n'.join(result))


def main():
	src_fileName = './待刷数据.xls'
	dst_fileName = './sql/refresh_resblock.sql'
	refresh_data_resblock(src_fileName,dst_fileName)

if __name__ == '__main__':
	main()