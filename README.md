# COLOR DETECTION and localization with OpenCV
Custom color Detection using OpenCV, Python.
# STEP 1 FIND CUSTOM COLOR VALUES
Editing the color value in source code and running the program, again and again, can be tedious, instead, you can bind trackbars to the output image window. Trackbar is a GUI element that let the user select a specific value within a range of values by sliding a slider linearly. It’s similar to scrolling but it limits the user to select a specific value with its minimum and maximum limits. A change in Trackbar value will result in a change in the mask. Create a mask of the desired color by changing the trackbar value to get a color value.
It is also possible to get multicolors under one range.
To get the color range values run "color_range_values.py" python file.
![red](https://user-images.githubusercontent.com/85798077/122750238-8b593380-d28e-11eb-8b30-b1e43854dca3.png)![multi_color](https://user-images.githubusercontent.com/85798077/122750289-98762280-d28e-11eb-92e7-da1b24dd19ad.jpg)
# STEP 2 DETECT CUSTOM COLOR IN IMAGE
After getting the values of color which is to be detected. It requires only to create a mask of those color values. To detect custom color run "color_detection.py" python file.
![blue_detection](https://user-images.githubusercontent.com/85798077/122751152-aed0ae00-d28f-11eb-946d-d263e9df8cc2.jpg)
# Color Localization
Locate specific color pixels in image. Draw rectangle where maximum pixels are present.
Python file: color_localization.py
![image](https://user-images.githubusercontent.com/85798077/177430019-1cc374c3-d2ad-493f-8180-5c8b893121da.png)
# Note
It is also possible to detect specific color objects of specific size. For that change the threshold value in "color_detection.py". The threshold value is then compared with the count of non-zero pixels present in the image after the mask.
