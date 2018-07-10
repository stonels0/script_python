# -*- coding: utf-8 -*-
# @Author: Lishi
# @Date:   2018-06-17 09:51:56
# @Last Modified by:   zhanglishi001
# @Last Modified time: 2018-06-26 12:09:24

import os,sys
import MySQLdb
import pdb

def queryVersion():
    # pdb.set_trace()
    database="192.168.10.10"	# "localhost"

    # 打开数据库：
    db = MySQLdb.connect(database,"homestead","secret","nts",charset='utf8')

    # 使用 cursor()方法获取操作游标;
    cursor = db.cursor()  # 当游标建立之时，就自动开始了一个隐形的数据库事务;

    # 使用execute方法执行SQl语句
    cursor.execute("SELECT VERSION()")

    # 使用fetchone()方法获取一条数据;
    data = cursor.fetchone()

    print("Database version : %s " %data)

    # 关闭数据库连接;
    db.close()
def create_table():
    dbName = "TESTDB"
    table = "EMPLOYEE"

    db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8')

    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS " +table);

    sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
    cursor.execute(sql)

    cursor.close()
    print("create table is succuss!!!")

def insertData():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8' )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 插入语句
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Json', 'Mohan', 18, 'W', 1000)"""
    # # SQL 插入语句
    # sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
    #        LAST_NAME, AGE, SEX, INCOME) \
    #        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    #        ('Mac', 'Mohan', 20, 'M', 2000)
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    
    # 关闭数据库连接
    db.close()

def queryData():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8' )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > '%d'" % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
            	(fname, lname, age, sex, income ))
                 
    except:
        print("Error: unable to fetch data ")


    db.close()


def updateData():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8' )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 更新语句
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行sql 语句;
        cursor.execute(sql)
        # 提交到数据库执行;
        db.commit()
    except:
        # 发生错误时 回滚;
        db.rollback()

    db.close()

def deleteData():
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8' )
    
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE < '%d'" % (15)
    try:
        # 执行sql 语句;
        cursor.execute(sql)
        # 提交修改;
        db.commit()
    except:
        # 发生错误时回滚;
        db.rollback()
    db.close()

def read_excel(filename):
    pdb.set_trace()
    import xlrd
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    # 获取所有sheet
    all_sheets_list = workbook.sheet_names()
    print(all_sheets_list) # [u'sheet1', u'sheet2']
    #获取sheet2
    sheet2_name= workbook.sheet_names()[1]
    print(sheet2_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_name('Sheet2')
    # sheet的名称，行数，列数
    print(sheet2.name,sheet2.nrows,sheet2.ncols)
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容
    print(rows)
    print(cols)
    #获取单元格内容的三种方法
    print(sheet2.cell(1,0).value.encode('utf-8'))
    print(sheet2.cell_value(1,0).encode('utf-8'))
    print(sheet2.row(1)[0].value.encode('utf-8'))
    # 获取单元格内容的数据类型
    print(sheet2.cell(1,3).ctype)

def read(file, sheet_index=0):
    import xlrd
    """

    :param file: 文件路径
    :param sheet_index: 读取的工作表索引
    :return: 二维数组
    """
    workbook = xlrd.open_workbook(file)
    # all_sheets_list = workbook.sheet_names()
    # print("本文件中所有的工作表名称:", all_sheets_list)
    # 按索引读取工作表
    sheet = workbook.sheet_by_index(sheet_index)
    print("工作表名称:", sheet.name)
    print("行数:", sheet.nrows)
    print("列数:", sheet.ncols)

    # 按工作表名称读取数据
    # second_sheet = workbook.sheet_by_name("b")
    # print("Second sheet Rows:", second_sheet.nrows)
    # print("Second sheet Cols:", second_sheet.ncols)
    # 获取单元格的数据
    # cell_value = sheet.cell(1, 0).value
    # print("获取第2行第1列的单元格数据:", cell_value)
    data = []
    for i in range(0, sheet.nrows):
        data.append(sheet.row_values(i))
    return data

def queryDict():

	result = {}
	filename = './role_nanjing.txt'
	with open(filename, 'r',encoding='utf8') as f:
		while True:
			line = f.readline()
			if not line:
				return result
			else:
				lines = line.strip().split('\t')
				key = lines[0].strip()
				value = lines[1].strip()
				result[key] = value
		return result

def generateSql(inFilename, outFilename, mapRoles):
    
    data = read(inFilename,7)

    strline = "INSERT INTO `sms_template`(`app_id`,`event_type`,`name`,`content`,`notify_role`,`notify_type`,`status`,`created_at`,`deleted_at`) values(320100,'"
    result =  []
    for id,line in enumerate(data, 1):
    	roles = line[0]
    	roles = roles.strip().split('/')
    	for i in range(len(roles)):
    		role = roles[i]
    		if not role or role == '短信接收人':
    			continue

    		sqlStr = strline + line[2] + "','"+line[1] +"','" +line[6] +"','"+ mapRoles[role] +"'," + "1,1,now(),now());"
    		result.append(sqlStr)
    with open(outFilename,'w',encoding='utf8') as f:
    	f.writelines('\n'.join(result))


def testCode():
	inFilename = './南京NTS开城-6-20-更正.xlsx'
	outFilename = './2018_06_26_320100_add_nanjing_sms_template.sql'
	mapRoles = queryDict()
	generateSql(inFilename, outFilename, mapRoles)
    # queryVersion()
    # create_table()
    # insertData()
    # queryData()
    # updateData()
    # deleteData()
    #filename = './test.xlsx'
    #print(read('test.xlsx'))
    #read_excel(filename)


def main():
    testCode()

if __name__ == '__main__':
    main()


