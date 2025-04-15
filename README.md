# 📸 Live Face Detection App with Streamlit & OpenCV

This project is a real-time face detection app that uses your webcam to detect faces and display them in a live video feed. Built with **OpenCV** for detection and **Streamlit** for the UI, it allows you to capture, display, customize, and save images with detected faces.

---

## 🧠 Key Features

- 🔴 **Live webcam streaming**
- 😎 **Real-time face detection** using Haar Cascades
- 🎨 Choose rectangle colors with a **color picker**
- 🛠 Tune detection parameters:
  - **Scale Factor**
  - **Minimum Neighbors**
- 📸 Capture and display still frames
- 💾 Save the captured face-detection image locally

---

## 📁 Project Structure

📂 live-face-detection-app/ │ ├── app.py # Main Streamlit interface ├── script.py # Face detection logic & color conversion ├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/live-face-detection-app.git
cd live-face-detection-app
pip install -r requirements.txt
You may need to install system dependencies for OpenCV and webcam support (e.g., portaudio, opencv-python, etc.).

📝 Requirements
Your requirements.txt should include:

nginx
Copy
Edit
streamlit
opencv-python
Optional:

nginx
Copy
Edit
Pillow
🚀 How to Run
bash
Copy
Edit
streamlit run app.py
🧩 This app must be run locally (Streamlit Cloud does not support webcam access).

🧠 script.py Breakdown
🔍 detect_face(...)
Detects faces from the webcam frame and draws rectangles around them.

python
Copy
Edit
def detect_face(vid_capture, scaleFactor, minNeighbors, colors)
vid_capture: the webcam video stream

scaleFactor: how much the image size is reduced at each scale

minNeighbors: how many neighbors each rectangle should have to be retained

colors: RGB tuple for the rectangle color

🎨 hex_to_rgb(...)
Converts hex color values (from Streamlit’s color picker) to RGB format for OpenCV.

python
Copy
Edit
def hex_to_rgb(hex_color)
🖼️ Output
Live video feed shows face rectangles

"Capture" button stores the current frame

"Save" button writes the image to a local file (captured_image.jpg)

🧑‍💻 Author
Ziggy Greg
GitHub • Instagram

📜 License
This project is licensed under the MIT License.
