import cv2

img = cv2.imread('photo.jpg')

# cv2.imshow('image',img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# print(img)
# print(img.shape)

print(len(img)) #682
print(len(img[0])) #683
print(len(img[0][0])) #3

newImg = []

for i in range(len(img)):
    for j in range(len(img[0])):
        # img[i][j][0] = 0 #blue
        # img[i][j][1] = 0 #green
        img[i][j][2] = 0 #red

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()