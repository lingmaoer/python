import re

string = '''taoyunjiaoyu
baidu''' #普通字符作为原子
pat1 = 'yun'
pat2 = '\n'
#-----------非打印字符---原子
'''
\n    \t制表符
\w   匹配字母，数字，下划线
\W   匹配除字母，数字，下划线
\d   十进制数    \D
\s     空白字符    \S
'''
rest1 = re.search(pat1,string)
rest2 = re.search(pat2,string)
print(rest1)
print(rest2)

#原子表
string1 = 'taoyunnnn4551516jiaoyubaidu'
pat3 = 'tao[xyz]un'
pat4 = 'tao[^abc]'
print(re.search(pat3,string1))
print(re.search(pat4,string1))

'''
#--------元字符-------
.    除换行以外的任意字符   一个
^    开始位置
$    结束位置
*     0/1/多次
？    0/1
+     1/多
{n}    恰好出现n次
{n,}   至少n次
{n,m}   至少n次，至多m次
|        模式选择符或
()       模式单元
'''
'''
pat5 = 'tao.un'
rest3 =re.search(pat5,string1)
print(rest3)

pat6 = '^tao....'
rest4 =re.search(pat6,string1)
print(rest4)

pat7 = "^ao..."
rest5 =re.search(pat7,string1)
print(rest5)

pat8 = "tao.*"
rest6 = re.search(pat8,string1)
print(rest6)

pat9 = "tao*"
rest7 = re.search(pat9,string1)
print(rest7)

pat8 = "tao.+"
rest6 = re.search(pat8,string1)
print(rest6)

pat8 = "taoyun+"
rest6 = re.search(pat8,string1)
print(rest6)

pat8 = "tao?"
rest6 = re.search(pat8,string1)
print(rest6)

pat8 = "yun{4}"
rest6 = re.search(pat8,string1)
print(rest6)

pat8 = "yun{2,}"
rest6 = re.search(pat8,string1)
print(rest6)

pat8 = "yun{1,3}"
rest6 = re.search(pat8,string1)
print(rest6)
'''

#-----模式修正符-----
'''
I    忽略大小写*
M    多行匹配*
U     Unicode
S     让.匹配包括换行*
'''
string = "Python"
pat1 = "pyt"
rest2 = re.search(pat1,string,re.I)
print(rest2)

#---贪婪模式--懒惰模式-----
string = "pooythonyptypjyy"
pat1 = "p.*y"#贪婪----模糊
rest2 = re.search(pat1,string,re.I)
print(rest2)
pat1 = "p.*?y"#懒惰---精准
rest2 = re.search(pat1,string,re.I)
print(rest2)

#正则表达式函数
#---match-----从头匹配

pat1 = "p.*?y"
rest2 = re.match(pat1,string,re.I)
print(rest2)

#---全局匹配-----

pat1 = "p.*?y"
rest2 = re.compile(pat1).findall(string)
print(rest2)

#实例
string = "<a href='http://www.baidu.com'>百度首页</a>"
pat = "[a-zA-Z]+://[^\s]*[.com|.cn]"
rset = re.search(pat,string)
print(rset)

#
string = "gvnwbj213-34555843yuyg9494-54578487y4578tngbhgdf"
pat = "\d{4}-\d{7}|\d{3}-\d{8}"
rset = re.compile(pat).findall(string)
print(rset)











































