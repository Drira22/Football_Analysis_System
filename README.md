# Football Analysis System (FAS)

## Overview

The **Football Analysis System** (FAS) is a machine learning and computer vision project designed to analyze football matches. This project detects players, referees, and footballs, tracks their movements, assigns players to teams based on t-shirt colors, and calculates metrics like player speed and distance covered. 

This work demonstrates how state-of-the-art tools like **YOLOv8** and **OpenCV** can be combined with clustering and optical flow techniques to solve real-world problems.

---
The input vide of this project will be found here:
https://drive.google.com/drive/u/0/folders/1DkFpqcfKM_QHPaT6UC12fedDfWHxdTt9?lfhs=2

---

## What We Did

1. **Object Detection with YOLOv8**:
   - Leveraged **Ultralytics YOLOv8** to detect objects such as players, referees, and footballs in video frames.
   - Fine-tuned a custom YOLO model to improve detection accuracy on our dataset.

2. **Object Tracking**:
   - Used tracking algorithms to follow the detected objects (players, ball, referees) across consecutive frames.
   - Generated object tracks for analyzing movement patterns.

3. **Team Assignment with KMeans**:
   - Used **KMeans clustering** to assign players to teams based on their t-shirt colors.
   - This helped differentiate between teams during gameplay analysis.

4. **Camera Movement Estimation**:
   - Implemented **optical flow** using OpenCV to estimate the camera’s movement between frames.
   - This step helps us analyze player motion in relation to the field and camera shifts.

5. **Video Output**:
   - Annotated videos with tracked objects, team assignments, and camera movements.
   - The output is saved as a processed video file demonstrating the analysis.

---

## What’s Next?

- **Perspective Transformation**:
  - Add depth and perspective to the analysis by transforming the scene to real-world coordinates.

- **Speed and Distance Calculation**:
  - Measure player speed and distance covered on the field in meters instead of pixels.

---

## Results

The processed video showcasing the results of the analysis can be found in the under this link : 
https://drive.google.com/drive/u/0/folders/1DkFpqcfKM_QHPaT6UC12fedDfWHxdTt9?lfhs=2


---

