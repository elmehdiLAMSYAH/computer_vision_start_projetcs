from LBPfeatures import LBP
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/WIN_20201029_16_26_48_Pro.jpg")
cv2.imshow("original picture",  image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow( "gray image" , gray_image)
cv2.waitKey(0)
" define a LBP object"
lbp = LBP(24, 8)

# computing the histogram
hist = lbp.describe(gray_image)
plt.hist(hist)
plt.show()
