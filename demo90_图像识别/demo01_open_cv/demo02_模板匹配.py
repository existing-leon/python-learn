import cv2
import numpy as np

# 读取原始图像和模板图像
img = cv2.imread('./data/example.jpg', 0)
template = cv2.imread('data/template.jpg', 0)
h, w = template.shape[:2]

# 进行模板匹配
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 获取匹配区域的左上角和右下角坐标
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# 提取四个角的像素点
top_left_pixel = img[top_left[1], top_left[0]]
top_right_pixel = img[top_left[1], bottom_right[0] - 1]
bottom_left_pixel = img[bottom_right[1] - 1, top_left[0]]
bottom_right_pixel = img[bottom_right[1] - 1, bottom_right[0] - 1]

# 打印四个角的像素点
print(f"左上角像素点值: {top_left_pixel}")
print(f"右上角像素点值: {top_right_pixel}")
print(f"左下角像素点值: {bottom_left_pixel}")
print(f"右下角像素点值: {bottom_right_pixel}")

# 在原始图像上绘制矩形框标记匹配区域
cv2.rectangle(img, top_left, bottom_right, 255, 2)

# 显示结果
cv2.imshow('Matching Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()