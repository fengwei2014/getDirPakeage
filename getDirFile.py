#打包脚本说明：
#必须包含文件：head.txt、endFile.txt、getDirFile.py

# -*- coding: utf-8 -*-
import re
import os

# 用正则匹配出每一行
def pareText(text):
    reg = r'(.*)'
    result = re.findall(reg, text)
    return list(result)

# 文本替换操作
# 给目录文件列表添加特定的格式
def replaceText(stringText):
    headText = 'F:/WMSPROJECT/WMS-PORTAL/WebContent/script'
    endText = '.js'
    changeHead = stringText.replace(headText, '"slf')
    changeEnd = changeHead.replace(endText, '",')
    result = changeEnd
    return changeEnd

# 文件合并
def joinFiles(inFiles, outFile):
    outfile = open(outFile, 'w+')

    errorfiles = []
    for infile in inFiles:
        try:
            in_file = open(infile, 'r')
            outfile.write(str(in_file.read()))
            in_file.close()
        except IOError:
            print 'error joining', infile
            errorfiles.append(infile)
    outfile.close()

# 获取文件目录
def getDirList(textlist, number, file_out):
    for i in range(0, number, 2):
        text = replaceText(textlist[i])
        file_out.write(text + '\n')
#
def traverse(path,depth=0):
    parePath = path
    result = parePath.replace('\\','/')
    reg = r'^\S+\.js$'
    m = re.match(reg,result)
    if(m != None):
            fileWriteIn.write('\t\t'+m.string+'\n')
    
    if(os.path.isdir(path)):
        for item in os.listdir(path):
            traverse(path+'/'+item, depth+1)
 

#path:目标js文件所在的文件路径
path = 'F:\WMSPROJECT\WMS-PORTAL\WebContent\script'
depth = 0
fileWriteIn = open('jsNameList.txt','w')
traverse(path,depth)
fileWriteIn.close()
print 'work done! find dirNamelsit in jsNameList.txt'+'\n'

file_object = open(r'jsNameList.txt')
file_out = open('out.txt', 'w+')
f_head = open('head.txt','r')
f_header = open('headFile.txt','w')

#项目名称
projectName = 'wms-portal'
#最终输出文件主文件名
projectFileOutName = 'mywmsportal'

try:
    text = f_head.read()
    text = text.replace('l-portal',projectName).replace('mylportal',projectFileOutName)
    f_header.write(text)
    f_head.close()
    f_header.close()
    all_the_text = file_object.read()
    textlist = pareText(all_the_text)
    number = len(textlist)
    getDirList(textlist, number, file_out)
    file_object.close()
    file_out.close()
    fileNameList = ("headFile.txt","out.txt","endFile.txt")
    outFilePath = 'wms-portal.profile.js'

    joinFiles(fileNameList, outFilePath)
finally:
    file_object.close()
    file_out.close()
    print 'find me in wms-portal.profile.js'
