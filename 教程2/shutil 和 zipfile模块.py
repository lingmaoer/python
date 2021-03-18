import shutil
import zipfile


#拷贝文件
# shutil.copyfile("CSV文件.csv","CSV文11.csv")

#拷贝文件夹
# shutil.copytree("","",ignore=shutil.ignore_patterns("*.text","*,txt"))

#压缩
#shutil.make_archive("goal_path","zip","original_path")

# z1 = zipfile.ZipFile("name.zip",'w')
# z1.write("")
# z1.close()

# 解压
# z2 = zipfile.ZipFile("name,zip",'r')
# z2.extractall("filename")
# z2.close()