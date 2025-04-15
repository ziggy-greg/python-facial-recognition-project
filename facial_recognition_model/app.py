import streamlit as st
import cv2
import tempfile
import os
from script import *  # Make sure this includes your detect_face() and hex_to_rgb() functions

cap = cv2.VideoCapture(0)

st.title("📷 Live Face Detection")
st.sidebar.header("📝 Instructions")
st.sidebar.markdown("""
1. Click **Start** to activate the webcam  
2. Click **Capture** to take a photo  
3. Adjust parameters (Scale, Neighbors, Rectangle Color)  
4. Click **Save** to store the image  
""")

# Parameter settings
st.sidebar.header("⚙️ Detection Parameters")
min_neighbour = st.sidebar.slider("Minimum Neighbors", 1, 10, 5, 1)
scale_factor = st.sidebar.slider("Scale Factor", 1.01, 2.0, 1.1, 0.01)
color_picker = st.sidebar.color_picker("Rectangle Color", '#ff0000')

frame_holder = st.empty()
start = st.button("Start")

if 'detect' not in st.session_state:
    st.session_state.detect = None

if start:
    stop = st.button("Capture")
    if not cap.isOpened():
        st.error("Camera not accessible. Please check permissions.")
    while cap.isOpened():
        rgb_color = hex_to_rgb(color_picker)
        img = detect_face(cap, scale_factor, min_neighbour, rgb_color)
        st.session_state.detect = img
        frame_holder.image(img, channels='RGB')
        if stop:
            break
    cap.release()

# Show image
show = st.button("Show Image")
if show:
    try:
        st.image(st.session_state.detect, channels='RGB', caption="📸 Captured Image")
    except:
        st.error("Press the Start button and Capture first.")

# Save image
save = st.button("Save Image")
if save:
    try:
        if st.session_state.detect is not None:
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, "captured_image.jpg")
            cv2.imwrite(temp_file, st.session_state.detect)
            st.success(f"Image saved successfully to: {temp_file}")
        else:
            raise ValueError("No image to save")
    except Exception as e:
        st.error(str(e))


