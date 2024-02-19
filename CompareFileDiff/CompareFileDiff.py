import sys
import glob
from difflib import *


def readfile(file1):
    try:
        fd=open(file1,"r", encoding = 'utf-8')
        text=fd.read().splitlines()  #讀取之後進行行分割
        return text
    
    except Exception as e:
        print("read file error")
        print(e)
        sys.exit()



def Compare(file_1,file_2):
    if file_1 =="" or file_2 == "":
        print("file 1 or file 2 not empty")
        sys.exit()

    text1=readfile(file_1)
    text2=readfile(file_2)

    d=Differ() #創建一個diff對象
    diff=d.compare(text1,text2)  #得出比較結果
    result = '\n'.join(diff)
    print(diff)
    print(result)

    try:
        fd_diff=open("diff.txt","w", encoding='utf-8')
        fd_diff.write(result)

    except Exception as e:
        print("write txt file error")
        print(e)
        sys.exit()

file1 = glob.glob('.\\file1\\*')[0]
file2 = glob.glob('.\\file2\\*')[0]

if __name__ == '__main__':
    Compare(file1,file2)