# -*- encoding: utf-8 -*-
# @Time     :2020/11/14 23:47
# @Author   :lingmao
# @File     :本质上升序列.py
# @Software :PyCharm

"""
【问题描述】
    小蓝特别喜欢单调递增的事物。
    在一个字符串中，如果取出若干个字符，将这些字符按照在字符串中的顺
    序排列后是单调递增的，则成为这个字符串中的一个单调递增子序列。
    例如，在字符串lanqiao 中，如果取出字符n 和q，则nq 组成一个单
    调递增子序列。类似的单调递增子序列还有lnq、i、ano 等等。
    小蓝发现，有些子序列虽然位置不同，但是字符序列是一样的，例如取第
    二个字符和最后一个字符可以取到ao，取最后两个字符也可以取到ao。小蓝
    认为他们并没有本质不同。
    对于一个字符串，小蓝想知道，本质不同的递增子序列有多少个？
    例如，对于字符串lanqiao，本质不同的递增子序列有21 个。它们分别
    是l、a、n、q、i、o、ln、an、lq、aq、nq、ai、lo、ao、no、io、lnq、
    anq、lno、ano、aio。
    请问对于以下字符串（共200 个小写英文字母，分四行显示）：（如果你把
    以下文字复制到文本文件中，请务必检查复制的内容是否与文档中的一致。在
    试题目录下有一个文件inc.txt，内容与下面的文本相同）
    tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhf
    iadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqij
    gihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmad
    vrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl
    本质不同的递增子序列有多少个？
【答案提交】
    这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一
    个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""
"""动态规划"""
string = """tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhf
            iadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqij
            gihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmad
            vrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl"""

sets = []
