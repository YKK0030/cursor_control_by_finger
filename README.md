# Hand Tracking Mouse Controller

This project uses hand tracking to control the mouse cursor on a computer. 

## Overview

- Uses the MediaPipe hand tracking solution to detect hands and finger positions
- Tracks the index finger tip to control mouse movement
- Detects pinching of index finger and thumb to trigger mouse clicks
- Works with a standard webcam input

## Usage

Run `main.py` with a webcam connected. Put your hand in the frame with fingers open. The index finger tip position controls the mouse movement on screen. Pinch the index finger and thumb together to trigger mouse clicks.

## Code

`main.py`
  - Main script, initializes camera, hand detector and runs main tracking loop
  
`HandTrackingModule.py`
  - Contains the handDetector class encapsulating the Mediapipe hand tracking functionality
  - Detects hands, tracks landmark points and provides useful methods like counting fingers
  
## Performance

- Runs at over 20 FPS on 720p webcam input 
- Sub-pixel accuracy in detecting finger landmark positions
- Can be customized by tweaking hand detection confidence parameters
