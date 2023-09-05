import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

#task one
def task_one(color_space, image_path):
   #saving image on image_path
   image_path = sys.argv[2]
   image = cv2.imread(image_path)
   if image is None:
    print("Error: Could not read the image")
    sys.exit(1)
  #passing color space
   color_space = sys.argv[1]

   if color_space == "-XYZ":
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
#spliting converted XYZ image to 3 diffrent scaled image
    X,Y,Z =cv2.split(converted_image)
#converting pixel value 0 to 255
    X_scaled = cv2.normalize(X, None, 0, 255, cv2.NORM_MINMAX)
    Y_scaled = cv2.normalize(Y, None, 0, 255, cv2.NORM_MINMAX)
    Z_scaled = cv2.normalize(Z, None, 0, 255, cv2.NORM_MINMAX)
 # Convert scaled components to 3-channel grayscale images
    X_gray = cv2.cvtColor(X_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    Y_gray = cv2.cvtColor(Y_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    Z_gray = cv2.cvtColor(Z_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    #stacking 2 image horizontally
    hori_image = np.hstack((image,X_gray))
   #stacking 2 image horizontally 
    hori_image2 = np.hstack((Y_gray,Z_gray))
    #stacking horizontal image vertically so it displays in a single viewing window
    verti_image=np.vstack((hori_image,hori_image2))

    
   elif color_space == "-Lab":
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    #spliting converted Lab image to 3 diffrent scaled image
    L,a,b =cv2.split(converted_image)
    #converting pixel value 0 to 255
    L_scaled = cv2.normalize(L, None, 0, 255, cv2.NORM_MINMAX)
    a_scaled = cv2.normalize(a, None, 0, 255, cv2.NORM_MINMAX)
    b_scaled = cv2.normalize(b, None, 0, 255, cv2.NORM_MINMAX)

    # Convert scaled components to 3-channel grayscale images
    L_gray = cv2.cvtColor(L_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    a_gray = cv2.cvtColor(a_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    b_gray = cv2.cvtColor(b_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
     #stacking 2 image horizontally
    hori_image = np.hstack((image,L_gray))
     #stacking 2 image horizontally
    hori_image2 = np.hstack((a_gray,b_gray))
    #stacking horizontal image vertically so it displays in a single viewing window

    verti_image=np.vstack((hori_image,hori_image2))

   elif color_space == "-YCrCb":
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    #spliting converted y,cr,cb image to 3 diffrent scaled image
    Y,Cr,Cb =cv2.split(converted_image)
    #converting pixel value 0 to 255
    Y_scaled = cv2.normalize(Y, None, 0, 255, cv2.NORM_MINMAX)
    Cr_scaled = cv2.normalize(Cr, None, 0, 255, cv2.NORM_MINMAX)
    Cb_scaled = cv2.normalize(Cb, None, 0, 255, cv2.NORM_MINMAX)
    # Convert scaled components to 3-channel grayscale images
    Y_gray = cv2.cvtColor(Y_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    Cr_gray = cv2.cvtColor(Cr_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    Cb_gray = cv2.cvtColor(Cb_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
         #stacking 2 image horizontally
    hori_image = np.hstack((image,Y_gray))
         #stacking 2 image horizontally
    hori_image2 = np.hstack((Cr_gray,Cb_gray))
    #stacking horizontal image vertically so it displays in a single viewing window
    verti_image=np.vstack((hori_image,hori_image2))

   elif color_space == "-HSB":
    converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H,S,B =cv2.split(converted_image)

    H_scaled = cv2.normalize(H, None, 0, 255, cv2.NORM_MINMAX)
    S_scaled = cv2.normalize(S, None, 0, 255, cv2.NORM_MINMAX)
    B_scaled = cv2.normalize(B, None, 0, 255, cv2.NORM_MINMAX)

    H_gray = cv2.cvtColor(H_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    S_gray = cv2.cvtColor(S_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    B_gray = cv2.cvtColor(B_scaled.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    hori_image = np.hstack((image,H_gray))
    hori_image2 = np.hstack((S_gray,B_gray))
    verti_image=np.vstack((hori_image,hori_image2))
   else:
    print("Error: Invalid color space option")
    sys.exit(1)

   #return final image
   cv2.imshow("Color Space Components", verti_image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()            

#task two
def task_two(scenicImageFile, greenScreenImagefile):
    scenic = cv2.imread(scenicImageFile)
    green_img= cv2.imread(greenScreenImagefile)
#resize both photo
    green_img_1 = cv2.resize(green_img, (740, 580))
    scenic_1 = cv2.resize(scenic, (740, 580))
#converting green image to hsv
    hsv = cv2.cvtColor(green_img_1, cv2.COLOR_BGR2HSV)
  
#setting upper and lower bound for green   
    u_green = np.array([60, 255, 255])
    l_green = np.array([36, 25, 25])
  #masking green image
    mask = cv2.inRange(green_img_1, l_green, u_green)
    #background is green and the object is black. masking is successful
    res = cv2.bitwise_and(green_img_1, green_img_1, mask= mask)
  #object is in original color and the background is black
    f = green_img_1 - res
  #object is in original color and the background is black
    g = green_img_1 - res
    #changing balck background to scenic background
    f = np.where(f == 0, scenic_1, f)
    #changing balck background to white background
    g[mask != 0] = 255
   #display all 4 picture in single viewing window
    hori_image = np.hstack((green_img_1,g))
    hori_image2 = np.hstack((scenic_1,f))
    verti_image=np.vstack((hori_image,hori_image2))
    cv2.imshow("Chromakey", verti_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()            





#taking input from terminal
#for task one
if len(sys.argv) == 3:
   if sys.argv[1] in ["-XYZ", "-Lab", "-YCrCb", "-HSB"]:
     task_one(sys.argv[1], sys.argv[2])
#for task two
   elif sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png") or sys.argv[1].endswith(".jpeg"):
     task_two(sys.argv[1], sys.argv[2]) 
  