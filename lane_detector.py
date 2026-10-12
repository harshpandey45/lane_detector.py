import cv2
import numpy as np

img = cv2.imread("road.jpg")

# grayscale and blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# canny edges
edges = cv2.Canny(blur, 50, 150)

# roi mask
h, w = edges.shape
mask = np.zeros_like(edges)
pts = np.array([[(0, h), (w // 2, int(h * 0.6)), (w, h)]], np.int32)
cv2.fillPoly(mask, pts, 255)
roi = cv2.bitwise_and(edges, mask)

# hough transform
lines = cv2.HoughLinesP(roi, 2, np.pi / 180, 100, minLineLength=40, maxLineGap=5)

line_img = np.zeros_like(img)
if lines is not None:
    for l in lines:
        x1, y1, x2, y2 = l[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 4)

res = cv2.addWeighted(img, 0.8, line_img, 1, 0)

cv2.imshow("output", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
