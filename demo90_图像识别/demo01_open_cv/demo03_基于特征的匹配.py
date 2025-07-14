import cv2
import numpy as np

# 读取原始图像和模板图像
img = cv2.imread('./data/example.jpg', 0)
template = cv2.imread('data/template.jpg', 0)

# 创建 ORB 特征检测器
orb = cv2.ORB_create()

# 检测关键点和描述符
kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(template, None)

# 创建 BFMatcher 对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 匹配描述符
matches = bf.match(des1, des2)

# 按距离排序
matches = sorted(matches, key=lambda x: x.distance)

# 获取匹配的关键点
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# 计算透视变换矩阵
M, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

# 获取模板图像的四个角点
h, w = template.shape
pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

# 进行透视变换
dst = cv2.perspectiveTransform(pts, M)

# 在原始图像上绘制匹配区域
img = cv2.polylines(img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

# 显示结果
cv2.imshow('Matching Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()