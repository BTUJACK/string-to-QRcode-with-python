

#把简历放进二维码，Python实现
#快速版
import qrcode
from PIL import Image
url = "\
姓名：Jack_ma\n\
年龄：40多\n\
身高：165左右 CM\n\
籍贯：杭州\n\
户籍：杭州\n\
住址：90年代的楼房\n\
邮箱：jack_ma@ali.com\n\
手机：18\n\
".strip()
img = qrcode.make(url)
img.show()





#装逼版，中间放个头像，顺便控制二维码大小

import qrcode
from PIL import Image
import os
#生成带logo的二维码图片
def make_logo_qr(str1,logo,save):
    #参数配置
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )
    #添加转换内容
    qr.add_data(str1)
    #
    qr.make(fit=True)
    #生成二维码
    img=qr.make_image()
    #
    img=img.convert("RGBA")
 
    #添加logo
    if logo and os.path.exists(logo):
        icon=Image.open(logo)
        #获取二维码图片的大小
        img_w,img_h=img.size
 
        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)
 
        #logo图片的大小不能超过二维码图片的1/4
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        #详见：http://pillow.readthedocs.org/handbook/tutorial.html
 
        #计算logo在二维码图中的位置
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
        #详见：http://pillow.readthedocs.org/reference/Image.html#PIL.Image.Image.paste
 
    #保存处理后图片
    img.save(save)
 

save_name='AI时代.png' #生成后的保存文件
logo='AI.png'  #logo图片

str1 = "\
姓名：Jack_ma\n\
年龄：40多\n\
身高：165左右 CM\n\
籍贯：杭州\n\
户籍：杭州\n\
住址：90年代的楼房\n\
邮箱：jack_ma@ali.com\n\
手机：18\n\
".strip()

make_logo_qr(str1,logo,save_name)



