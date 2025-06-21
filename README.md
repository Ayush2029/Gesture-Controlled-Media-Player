# Gesture-Controlled-Media-Player

This project enables you to control media playback on your computer using hand gestures, leveraging your webcam and the power of computer vision. It's built with Python, utilizing OpenCV for camera interaction, MediaPipe for hand tracking, and PyAutoGUI for simulating keyboard presses. <br>

<h3>Features: </h3>
🖐️ Hand Gesture Recognition: Detects the number of extended fingers to interpret commands. <br>
▶️ Media Playback Control:<br>
1 Finger: Fast forward 5 seconds (simulates "right arrow" key).<br>
2 Fingers: Rewind 5 seconds (simulates "left arrow" key).<br>
3 Fingers: Increase volume by 5% (simulates "up arrow" key).<br>
4 Fingers: Decrease volume by 5% (simulates "down arrow" key).<br>
5 Fingers: Play/Pause video (simulates "spacebar" key).<br>
✨ Real-time Visual Feedback: Displays your webcam feed with overlaid hand landmarks. <br>
⚙️ Gesture Debouncing: Prevents accidental multiple actions from quick, unintentional gestures. <br>
