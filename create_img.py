import cv2
import numpy as np 
import random 
np.set_printoptions(threshold=np.inf)


img = np.zeros((1000,1000,3))


for i in range(500):
    for j in range(500-i):
        img[i][j] = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]

for i in range(1000):
    if(i<=500):
        for j in range(500-i,1000,1):
            img[i][j] = [0,255,0]
    else:
        for j in range(0,1500-i,1):
            img[i][j] = [0,255,0]
    
for i in range(500,1000):
    for j in range(1500-i,1000,1):
        img[i][j] = [random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]

#print(img)
        
cv2.imshow("Diagonal Image RBG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Diagonal_RBG_Image.png",img)

# ast = cv2.imread("image.png")
# print(ast)


# """
# for i in range(100): 
#     for j in ast.shape[1]:
#         ast[i][j] = 
# """
# print()