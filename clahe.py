import cv2
import numpy as np
import glob
import os
from os import listdir


print("-------------------------------------------")
print("------------   Clahe Image  -----------")
print("-------------------------------------------")

#set target folder path
print("Enter image folder path: ")
TARGET_PATH = input()

#make destin folder
DESTIN_PATH = TARGET_PATH+"/Clahe_Image"
if not os.path.exists(DESTIN_PATH):
	os.makedirs(DESTIN_PATH)

images = [cv2.imread(image) for image in glob.glob(TARGET_PATH+"/*.jpg")]

cnt=0
for filename in listdir(TARGET_PATH):
	if not(filename.startswith('.') or os.path.isdir(TARGET_PATH + '/' +filename)):
			# Resizing the image for compatibility
			images[cnt] = cv2.resize(images[cnt], (500, 600))
			gray = cv2.cvtColor(images[cnt], cv2.COLOR_BGR2GRAY)
			clahe = cv2.createCLAHE(clipLimit = 5)
			final_img = clahe.apply(gray) + 30
			cv2.imwrite(DESTIN_PATH+"/"+filename,final_img)
			cnt=cnt+1
			#cv2.imshow("clahed_image", final_img)
			
			#cv2.waitKey(0)
			#cv2.destroyAllWindows()


print("<<<<<<<<<<<<<<<<<<<<<<<  ALL DONE!   >>>>>>>>>>>>>>>>>>>>>>>")


	




	

        



