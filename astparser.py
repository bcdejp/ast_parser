# -*- coding: utf-8 -*-

import re

# ネストの深さとテキスト内容を取得する
def get_branch_index(s):
    x = s.find('|-')
    y = s.find('`-')
    if x < y:
        x = y
    content = s
    if x >=0:
        content = content[x+2:]
    return x, content

# メイン処理

# ファイルをオープンする
astfile = open("./sample/input.ast", "r")

for line in astfile:
    line = line.replace('\n','')
    #print(line)
    index,content = get_branch_index(line)
    #print(content)

    print("-----")

    # 関数の抽出(used)
    pattern = 'FunctionDecl (0x[0-9a-z]+) <.*?> .+ used (.+?) (.*)'
    result = re.match(pattern, content)
    if result:
        #print(result.group())# group()で全文字を
        print(result.group(1))# ID
        print(result.group(2))# 関数名
        print(result.group(3))# 戻り値&引数

    print("-----")

    # 関数の抽出(prev)
    pattern = 'FunctionDecl (0x[0-9a-z]+) prev (0x[0-9a-z]+) <.*?> .+ used (.+?) (.*)'
    result = re.match(pattern, content)
    if result:
        #print(result.group())# group()で全文字を
        print(result.group(1))# ID
        print(result.group(2))# ID
        print(result.group(3))# 関数名
        print(result.group(4))# 戻り値&引数    
    
astfile.close()