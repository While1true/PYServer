import jieba
import re

from masterWeiBo.Utils.Sql import  Mydb as db

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


cursor = db().cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS `weibo`.`masterWeiBo_analysis` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `count` INT NOT NULL DEFAULT 0,
  `category` VARCHAR(100) NOT NULL,
  `wordsTop10` VARCHAR(1000) NULL,
  PRIMARY KEY (`id`));""")
cursor.execute("DELETE FROM weibo.masterWeiBo_analysis")
cursor.execute("SELECT count(id) as countd, category as category FROM weibo.masterWeiBo_master GROUP BY category")
results = cursor.fetchall()
print(results)
dicts=[]
stopwords = stopwordslist("words.txt")
for result in results:
    each={}
    each['count']=result['countd']
    each['category']=result['category']
    print(result['countd'])
    print(result['category'])
    cursor.execute("SELECT content from weibo.masterWeiBo_master where category = '"+result['category']+"'")
    contents = cursor.fetchall()
    articals=''
    for artical in contents:
        articals+=","+artical['content']
    cuts = jieba.cut(articals)
    words={}
    for cut in cuts:
        if(cut in words):
            words[cut]=words[cut]+1
        else:
            words[cut]=1
    sortedWords = sorted(words.items(), key=lambda d: d[1], reverse=True)
    wordsTop10=''
    i=0
    for key ,value in sortedWords:
        if(key in stopwords or key.__len__()<2):
            continue
        wordsTop10+=key+","+str(value)+";"
        i+=1
        if(i==10):
            wordsTop10=wordsTop10[:wordsTop10.__len__()-1]
            break
    each['wordsTop10']=wordsTop10
    dicts.append(each)
for value in dicts:
    sql = "INSERT INTO weibo.masterWeiBo_analysis (count,category,wordsTop10) values( '" + str(
        value['count']) + "','" + value['category'] + "','" + value['wordsTop10'] + "')"
    print(sql)
    cursor.execute(sql)
cursor.close()
print(dicts)
