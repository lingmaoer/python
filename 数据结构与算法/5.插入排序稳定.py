# [54, 226, 93, 17, 77, 31, 44, 55, 20]  #升序排序

def insert_sort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                list[j] ,list[j-1]=list[j-1],list[j]
                print(list)

# def insert_sort(alist):
#     n=len(alist)
#     for j in range(1,n):  #n-1   n
#         i=j
#         while i>0: #和有序列表中每个元素进行比较 （从最后一个开始）
#             if alist[i]<alist[i-1]: #如果当前元素比前一个元素小，则进行交换
#                 alist[i],alist[i-1],=alist[i-1],alist[i]
#                 print(alist)
#             else:#否则已经是有序列表，不需要交换了，则退出循环
#                 break
#             i-=1

list= [54, 226, 93, 17, 77, 31, 44, 55, 20]
print(list)
insert_sort(list)
print(list)