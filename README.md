# Gesture-Controlled-Media-Player

This project enables you to control media playback on your computer using hand gestures, leveraging your webcam and the power of computer vision. It's built with Python, utilizing OpenCV for camera interaction, MediaPipe for hand tracking, and PyAutoGUI for simulating keyboard presses. <br>

<h3>Features: </h3>
(1) 🖐️ Hand Gesture Recognition: Detects the number of extended fingers to interpret commands. <br>
(2) ▶️ Media Playback Control:<br>
- 1 Finger: Fast forward 5 seconds (simulates "right arrow" key).<br>
- 2 Fingers: Rewind 5 seconds (simulates "left arrow" key).<br>
- 3 Fingers: Increase volume by 5% (simulates "up arrow" key).<br>
- 4 Fingers: Decrease volume by 5% (simulates "down arrow" key).<br>
- 5 Fingers: Play/Pause video (simulates "spacebar" key).<br>
(3) ✨ Real-time Visual Feedback: Displays your webcam feed with overlaid hand landmarks. <br>
(4) ⚙️ Gesture Debouncing: Prevents accidental multiple actions from quick, unintentional gestures. <br>

<h3>🛠️ Installation </h3>
Follow these steps to get the project up and running on your local machine. <br>
Prerequisites: <br>
- Python 3.x: Make sure you have Python installed. You can download it from python.org. <br>
<br>
Step-by-Step Installation <br>
1] Clone the Repository: <br>
- Open your terminal or command prompt and clone the project repository to your local machine. <br>
  git clone https://github.com/your-username/hand-gesture-media-controller.git <br>
- Navigate into the cloned project directory: <br>
<br>
2] Install Dependencies: <br>
Once you're in the project directory, install all the required libraries using the requirements.txt file: <br>
pip install -r requirements.txt <br>

<h3>🏃 How to Run </h3>
- Once you have installed the dependencies, you can run the main script: <br>
python Gesture controlled Media Player.py <br>
- A window will pop up displaying your webcam feed. Position your hand clearly in front of the camera to start controlling your media! <br>

<h3>✋ How to Use: </h3>
Simply show your hand to the webcam with the corresponding number of fingers extended to perform an action:<br>
- 1 Finger: Forward <br> 
- 2 Fingers: Backward <br>
- 3 Fingers: Volume Up <br>
- 4 Fingers: Volume Down <br>
- 5 Fingers: Play/Pause <br>
Press the ESC key to exit the application. <br>

<h3>💡 Troubleshooting </h3>
(1) Webcam not detected: Ensure your webcam is properly connected and not in use by another application. <br>
(2) Permissions: On some operating systems, you might need to grant camera access permissions to your terminal or IDE. <br>
(3) Gesture Sensitivity: If gestures are not consistently recognized, try adjusting the lighting or the distance of your hand from the camera. <br>
(4) PyAutoGUI Issues: If pyautogui doesn't seem to press keys, ensure your media player is the active window. Also, be aware that pyautogui might require specific permissions on macOS. <br>
