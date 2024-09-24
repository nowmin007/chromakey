# chromakey
chroma key using open CV. replace green screen with bakground image or video.
Objectives
 Getting familiar with OpenCV 4.6.0
 Reading, processing and displaying images using OpenCV 4.6.0
 Understanding color spaces
Task One
Many color spaces are available to represent pixel values of a color image. Some are perceptually uniform and others are not. This task is to read an image and display the original color image and its components of a specified color space, such as CIE-XYZ, CIE-Lab, YCrCb and HSB. The color components must be displayed in gray-scale. The original image and its three components must be display in a single viewing window as arranged below.
Original Image
C1(e.g.X,L,Y orB)![img2](https://github.com/user-attachments/assets/84e05214-465b-48c4-bfa0-6b7fcdd9ced7)

C2 (e.g. Y, a, Cr or H)
C3 (e.g. Z, b, Cb, or S)
Note that
a) RGB color space is commonly used to represent a digitized images and each color component, also known as a color channel, is digitized into unsigned 8 bits, i.e. the possible values for each component ranges from 0 to 255. (See Appendix: Digital Representation of Images)
b) a JPG image file is often decoded into a RGB image, RGB values of each pixel may be packed together with an alpha channel into 32 bits for efficient access by CPU. The value of alpha channel may be ignored or may be used for transparency as needed. When a JPG image is loaded by an OpenCV function, such as imread(...), please check OpenCV online reference to understand how the RGB values of each pixel is packed and stored, and make sure you access these values correctly. (See Appendix: Digital Representation of
1 of 5
SCIT, University of Wollongong
Images)
c) For a color space other than RGB, check the range of its valid values for each component
and you may need to scale the color component values properly so as to display the components in gray-scale images whose pixel values are between 0 to 255, i.e. 8 bits; Note that a gray-scale image means that the RGB values are same for each pixel.
Images are provided to test/debug your code. It is highly recommended that you create testing cases by yourself.
Task Two
A Chroma key is a technique used in film, television studio and photography to replace a portion of an image with a new image or to place a person, such as a newsreader, on a scenic background. Below shows an example:
Source: http://mediacollege.com
You are provided with a few photos of a single person in front of a green screen, referred to as green screen photos, and a few scenic photos. This task is to extract the person in a green screen photo using appropriate Chroma information, e.g. hue and/or other Chroma information, and place the person in a scenic photo according to the following:
a) The combined photo should be of the same size as the scenic photo, and
b) The person should be aligned horizontally to the middle of the scenic photo
The program should display in a single viewing window the photo of a person in front of a green screen, person extracted from the green screen photo with white background, scenic photo, photo with the person being in the scenic in a single viewing window as illustrated below.
         (a) A green screen photo with subjects
    (b) Subjects extracted from the green screen photo are blended with a scenic photo
    Photo of a person with green screen
Photo of the same person with white background
Scenic photo
The same person in the scenic photo
2 of 5

SCIT, University of Wollongong
Requirements on implementation
1. The program should be named as “Chromakey” and shall take
a. one filename and one of the options –XYZ, -Lab,-YCrCb or -HSB as the
command argument for Task One, e.g.
Chromakey –XYZ|-Lab|-YCrCb|-HSB imagefile # task one or
b. two filename as the command arguments for Task Two, e.g.
Chromakey scenicImageFile greenScreenImagefile # task two
2. The size of the viewing window for both tasks should not be over the size of 1280 × 720
(width x height pixels) on either dimension, but should not be too small.
3. There should not be any gap between images in the viewing window. One way is to combine the four images to be displayed into a single one then display the combined one
using imshow() in OpenCV
4. Aspect ratios of all images must be kept unchanged while they are being displayed in the
viewing window.
5. No other third-party libraries should be used in the program except OpenCV 4.6.0. The code
has to be in Python (with OpenCV 4.6.0, assuming numpy and matplotlib packages
exist).
6. The code should be modularized with detail comments AND all source code should be
placed in a single file named as “Chromakey.py”.
