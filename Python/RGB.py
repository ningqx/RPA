from PIL import Image

# 输入待识别图片地址，请使得图片大小大于30像素
img = Image.open('1.png')
box = (10, 10, 20, 20)
roi = img.crop(box)
img2 = roi.convert('RGB')
colors = img2.getcolors(img2.size[0] * img2.size[1])
r,g,b =colors[0][1]

hex_string ='#{:02X}{:02X}{:02X}'.format(r, g, b)
# 输出图片16进制颜色，并保存到当前目录下的1.txt中
with open('1.txt','w') as f:
    f.write(hex_string)




