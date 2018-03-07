#encoding:utf_8
import pymysql
import sys
print(sys.getdefaultencoding())
sys.setdefaultencoding('utf8')
import threading
class Mydb(object):
    tableName='master'
    def __init__(self):
        self.lock=threading.Lock()
        self.client = pymysql.connect(host='localhost',charset='utf8', port=3306, user='root', passwd='ck123', db='weibo')
        self.client.autocommit(True)
        self.cursor = self.client.cursor()
        self.insertSql = "INSERT INTO weibo.master(%s) VALUES (%s)"
        self.querySql = "SELECT %s from weibo.master where %s "

    def close(self):
        self.client.close()

    def getCurser(self):
        return self.client.cursor()

    def getInsertSql(self, message):
        cckey = ''
        ccvalue = ''
        for key, value in message.items():
            cckey += key + ','

            if (type(value) is list):
                valu = ''
                for iv in value:
                    valu += iv + ';'
                value = valu[:-1]
            ccvalue += "'" + str(value) + "',"
        cckey = cckey[:-1]
        ccvalue = ccvalue[:-1]
        sql = self.insertSql % (cckey, ccvalue)
        return sql
    def getQuerySql(self,keys,wheres):
        sql=self.querySql % (keys,wheres)






