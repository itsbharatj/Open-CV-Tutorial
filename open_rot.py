import cv2
img_org = cv2.imread('image.png',1)
img_gry = cv2.imread('image.png',0)

img_org_half = cv2.resize(img_org,(0,0),fx=0.5,fy=0.5)
cv2.imwrite("Half_Size.png",img_org_half)



cv2.imshow("Half size",img_org_half)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imshow("Astronout in the Jungle",img_org)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("In Grayscale:",img_gry)
cv2.waitKey(0)
cv2.destroyAllWindows()

