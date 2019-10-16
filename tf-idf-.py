import jieba.analyse
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.feature_extraction.text import CountVectorizer
import os
import re
#import codecs
import math
import operator

def writefile(path, content):
    with open(path, "a", errors="ignore", encoding="utf-8") as file:
        wordlist = content.split(" ")
        for word in wordlist:
            file.write(word + "\n")
        #file.write(content)

def tf(inputpath, outputpath):
    RE = re.compile(u'[\u4e00-\u9fa5]', re.UNICODE)
    swlis = []
    with open("stop.txt", "r", errors="ignore", encoding='utf-8') as file:
        for line in file:
            outsw = line.replace('\n', '')
            swlis.append(outsw)
    contentpath = os.listdir(inputpath)
    for childpath in contentpath:
        cpath = inputpath + childpath
        with open(cpath, "r", errors="ignore", encoding='utf-8') as file:
            for content in file:
                afterswlis = ""
                content = content.strip()
                contents = content.replace("  ", " ")
                contents = contents.split(" ")
                for j in contents:
                    if str(j) in swlis:
                        continue
                    else:
                        match = re.search(RE, j)
                        if match is None:
                            continue
                        else:
                            afterswlis += j
                keywords_tfidf = jieba.analyse.extract_tags(afterswlis, topK=20, withWeight=False)
                print(keywords_tfidf)
                writefile(outputpath + childpath, str(keywords_tfidf) + "\n")


if __name__ == '__main__':
    #jieba.load_userdict("dict.txt")
    tf("C:/Users/weiyu/Desktop/文本特征关键字提取/data/","C:/Users/weiyu/Desktop/文本特征关键字提取/result/")