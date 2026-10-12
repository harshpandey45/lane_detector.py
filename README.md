# road-lane-detector

Simple computer vision script to detect road lane lines on an image using OpenCV.

### Flow
- Grayscale & Gaussian Blur
- Canny Edge Detection
- ROI polygon mask (road focus)
- Hough Line Transform to draw lane boundaries

### Requirements
- python 3.x
- opencv-python
- numpy
