import MeCab
import sys
import re
from collections import Counter

#変換データ
dic = {'会社':'ハッテン場','仕事':'デカマラ','残業時間':'ケツマンコタイム','残業':'ケツマンコ'}

# ファイル読み込み

infile = 'input\\test.txt' 
with open(infile ,encoding="utf-8") as f:
    data = f.read()
print('\n')
print('変換前')
print(data)

print('変換後')
with open(infile ,encoding="utf-8") as f:
    data = f.readlines()

tagger = MeCab.Tagger("-Ochasen")

for dataItem in data:
    parse = tagger.parse(dataItem)
    lines = parse.split('\n')
    items = (re.split('[\t,]', line) for line in lines)

    #1行分の出力用変数
    outputLine = ''
    zenkai = ''
    # 結果を表示
    for item in items:
    
        output = item[0]
        
        #EOSが来たら1行分出力
        if output == 'EOS':
            zenkai = ''
            print(outputLine)
            break
        
        #前回が数値で、今回が時間とかなら本にする
        if (zenkai == '名詞-数'):
            if ( output == '時間' or output == '分' ) :
                output = '肉棒' + zenkai_num + '本分'
            else:
                outputLine += zenkai_num 

        #変換候補に一致するなら変換する
        if output in dic:
            output = dic[output]
        
        #出力用変数に値格納
        if (item[3] == '名詞-数'):
            zenkai_num = item[0]
        else:
            outputLine += output

        zenkai = item[3]
print('\n')

