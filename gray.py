import cv2

img = cv2.imread("/Users/mvpzhao/data/tianchi-mtwi/icpr_mtwi_task1/test_line_image/line_1.jpg", 0)

# Otsu 滤波
ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite("black.jpg", binary)
