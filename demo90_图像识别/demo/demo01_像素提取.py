import time

from PIL import Image

# pic_path = './data/屏幕截图01.png'
pic_path = './data/屏幕截图02.png'

resolution_ratio_x = 1080
resolution_ratio_y = 1920
y_pianyi = 0

pic = Image.open(pic_path)
pic_new = pic.convert('RGBA')
pix = pic_new.load()
for x in range(41, 410):
    if 194 <= \
            pix[x * resolution_ratio_x // 1080, 360 * resolution_ratio_y // 1920 + y_pianyi][
                0] <= 200 and 187 <= \
            pix[x * resolution_ratio_x // 1080, 360 * resolution_ratio_y // 1920 + y_pianyi][
                1] <= 193 and 241 <= \
            pix[x * resolution_ratio_x // 1080, 360 * resolution_ratio_y // 1920 + y_pianyi][
                2] <= 247:  # 判定存在小福袋的图标
        last_find_fudai_time = time.time()
        print(f'===> x = {x}')
