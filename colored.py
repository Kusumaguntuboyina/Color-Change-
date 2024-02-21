import cv2
img=cv2.imread('color.jpg')
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey.jpg',gry)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imwrite('rgb.jpg',rgb)

