#
# import  urllib.request
#
# urlopen = urllib.request.urlopen(
#     "http://tyyh.fjbs.gov.cn/ca_service/rest/ca/token?app_id=23630FC9F0E512F46A765AEA15958C7E&app_secret=fj_szgjj@0226", )
#
# read = urlopen.read()
# print(read)

# wordcloud生成中文词云

from wordcloud import WordCloud
import codecs
import jieba
# import jieba.analyse as analyse
# from scrapy.utils imread
from imread import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# pwd = os.getcwd()
# father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
# pathx = father_path + os.path.sep + "static" + os.path.sep


# 绘制词云
def draw_wordcloud(word, name,pattern):
    # 读入一个txt文件
    # comment_text = open('F:\program\MyProjects\clustering\\fenci1.0\wordseg_result.txt','r').read()
    # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(word))
    # 当前文件的路径
    # path = pathx + name
    color_mask =None
    if(pattern):
        try:
            color_mask=imread(pattern) # 读取背景图片
        except Exception:
            pass
    cloud = WordCloud(
        # 设置字体，不指定就会出现乱码
        font_path=r"msyh.ttc",
        # font_path=path.join(d,'simsun.ttc'),
        # 设置背景色
        background_color='white',
        width=1080,
        height=1920,
        # 词云形状
        mask=color_mask,
        # 允许最大词汇
        # max_words=2000,
        # #最大号字体
        # max_font_size=400,
        # min_font_size=200
        scale=1.5
    )
    word_cloud = cloud.generate(cut_text)  # 产生词云
    word_cloud.to_file("static/pic/" + name)  # 保存图片
    # return path


#  显示词云图片
# plt.imshow(word_cloud, interpolation="bilinear")
# plt.axis('off')
# plt.show()
from public.GLOBAVARS import WORDPRESS_HOST as host


def generatePic(word, md5name,pattern=None):
    pathx = "static/pic/" + str(md5name) + ".jpg"
    if (os.path.exists(pathx)):
        return host + str(md5name) + ".jpg"
    else:
        draw_wordcloud(word, str(md5name) + ".jpg",pattern)
        return host + str(md5name) + ".jpg"


if __name__ == '__main__':
    print(generatePic("xxxxxrere股骨头规范教育局UIUC", 100))
    # draw_wordcloud("道德经大家","123.jpg")
