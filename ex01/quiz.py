masuo = ["マスオ","ますお","マスオさん","ますおさん"]
wakame = ["ワカメ","わかめ"]
oi = ["甥","おい","甥っ子","おいっこ"]

import datetime
import random

def quiz_m():
    ans_m = input("サザエの旦那の名前は？:")
    if ans_m in masuo:
        print("正解")
    else:
        print("不正解")

def quiz_w():
    ans_w = input("カツオの妹の名前は？:")
    if ans_w in wakame:
        print("正解")
    else:
        print("不正解")

def quiz_o():
    ans_o = input("タラオはカツオから見てどんな関係？:")
    if ans_o in oi:
        print("正解")
    else:
        print("不正解")

r = random.randint(0,2)
st = datetime.datetime.now()
if r == 0:
    quiz_m()
    ed = datetime.datetime.now()
elif r == 1:
    quiz_w()
    ed = datetime.datetime.now()
else:
    quiz_o()
    ed = datetime.datetime.now()
print((ed-st).seconds)