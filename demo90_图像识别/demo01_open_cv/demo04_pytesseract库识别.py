import os
import cv2
import pytesseract

# 设置Tesseract的路径（根据实际情况修改）
pytesseract.pytesseract.tesseract_cmd = r'D:\develop\python\Tesseract-OCR\tesseract.exe'

# 设置TESSDATA_PREFIX环境变量（根据实际情况修改）
os.environ['TESSDATA_PREFIX'] = r'D:\develop\python\Tesseract-OCR\tessdata'

# 读取图像
image = cv2.imread('./data/chepai.jpg')

# 图像预处理
# 1. 灰度化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. 降噪（可选）
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. 二值化
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 使用pytesseract进行文字识别，同时指定中文和英文
text = pytesseract.image_to_string(thresh, lang='chi_sim+eng')

# 输出识别结果
print("识别结果：")
print(text)

# 显示原始图像和预处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()