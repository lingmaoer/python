"""
import cv2

#读取文件
image = cv2.imread('')
#加载人脸模型
face_model = cv2.CascadeClassifier("facemodel.lxml")
#灰度处理
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#检查人脸
faces = face_model.detectMultiScale(gray)
#标记人脸
for (x,y,w,h) in faces:
    #rectangle 矩形  (原始图片 ，左上角点，右下角点，线的颜色，线宽
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),10)
#显示图片
cv2.imshow("tupian",image)
#暂停窗口
cv2.waitKey(0)
#释放资源
caputre.release()
#销毁
cv2.destroyAllwindows()

"""
import cv2

#打开摄像头
caputre = cv2.VideoCapture(0)
#模型
face_model = cv2.CascadeClassifier("facemodel.lxml")
#获取摄像头画面
while True:
    #读取每一帧
    res,image = caputre.read()

    #灰度
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #检查人脸
    faces = face_model.detectMultiScale(gray)
    # 标记人脸
    for (x, y, w, h) in faces:
        # rectangle 矩形  (原始图片 ，左上角点，右下角点，线的颜色，线宽
        cv2.rectangle (image, (x, y), (x + w, y + h), (0, 255, 0), 10)
        #显示图片
        cv2.imshow("tupian",image)
        #暂停窗口
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break
#释放资源
caputre.release()
#销毁
cv2.destroyAllwindows()



