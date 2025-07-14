import cv2

# 读取图像
image = cv2.imread('data/example.jpg')

# 显示图像
cv2.imshow('Image', image)

# 等待按键事件
cv2.waitKey(0)

# 关闭所有窗口
cv2.destroyAllWindows()