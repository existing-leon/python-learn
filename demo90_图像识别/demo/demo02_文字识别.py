import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

ocr = PaddleOCR()


def analyse_pic_word(pic_path='', change_color=0):
    img = Image.open(pic_path)
    img = img.convert('L')  # 转换为灰度图
    if change_color == 1:
        img = img.point(lambda x: 0 if x < 128 else 255)  # 二值化
    elif change_color == 2:
        img = img.point(lambda x: 0 if x < 251 else 255)  # 二值化
    img_np = np.array(img)  # 将 Image 对象转换为 numpy 数组
    result = ocr.ocr(img_np)
    if result == [None]:
        return ''
    return extract_ocr_content(result)


def extract_ocr_content(content=[]):
    """对OCR识别到的内容进行取值和拼接，变成完整的一段内容"""
    ocr_result = content
    extracted_content = []
    for item in ocr_result[0]:  # item 的结构为 [位置信息, (识别内容, 置信度)]
        extracted_content.append(item[1][0])
    contains = ''.join(context for context in extracted_content if context)
    return contains


if __name__ == '__main__':

    template = '豫S·2128Z'
    # pic_path = './pic/chepai.png'
    pic_path = './pic/chepai.jpg'
    # pic_path = 'pic/jietu.png'
    # pic_path = 'pic/jietu01.png'
    # pic_path = 'pic/jietu02.png'
    change_color = 1
    text = analyse_pic_word(pic_path, change_color)
    print(f'图片中的文本为：\n{text}')
    if text == template:
        print(f'{template} 车主, 欢迎您回家!')
    pass
