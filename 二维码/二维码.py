import qrcode  # 生成普通二维码


def make_coke():
    qr = qrcode.QRCode(
        version=5,  # 版本,大小
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 误差值
        box_size=8,  # 像素格
        border=4,  # 单元格
    )
    qr.add_data("俊才")  # 二维码内容
    qr.make(fit=True)  # 生成二维码
    img = qr.make_image()  # 生成图片
    img.save("abc.png")  # 名字
    img.show()


make_coke()

# from MyQR import myqr
#
# qr = myqr.run(
#     words="12345",#生成数据，不支持中文
#     version=5,
#     level='L',
#     picture="QQ图片20200327160107.gif",
#     colorized= True,#是否彩色
#     contrast=1.0, #对比度
#     brightness=1.0,
#     save_name='2467078112.gif',
#     save_dir="E:\\biancheng\\python\\二维码"
# )
