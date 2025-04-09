import streamlit as st
import cv2
import tempfile
import os
from script import *

cap = cv2.VideoCapture(0)

st.title("Live Face Detection")
st.sidebar.header("Instructions")

st.sidebar.write("1. Click the 'Show' button to display Image")
st.sidebar.write("2. Click the 'Start' button to activate your webcam")
st.sidebar.write("3. Click the 'Capture' button to take a photo and clicking the 'Start' button")
st.sidebar.write("4. Adjust the parameters to your need or choice")
st.sidebar.write("5. Click the 'Save' button to Save your image")


st.sidebar.header("Parameters")
min_neighbour = st.sidebar.slider("Minimum Neigbour", min_value=1, max_value=10, value=5, step=1)
scale_factor = st.sidebar.slider("Scale Factor", min_value=1.01, max_value=2.0, value= 1.1, step=0.01)
color_picker = st.sidebar.color_picker("Choose the color of your choice for the rectangle", '#ff0000')

frame_holder = st.empty()
start = st.button("Start")

if 'detect' not in st.session_state:
    st.session_state.detect = None

if start:
    stop = st.button("Capture")
    while cap.isOpened():
        rgb_color = hex_to_rgb(color_picker)
        img= detect_face(cap, scale_factor, min_neighbour, rgb_color)
        st.session_state.detect = img
        frame_holder.image(img, channels='RGB')
        if stop:
            break

    cap.release()    
show = st.button("Show Image")    

try:
    if show:
        st.image(st.session_state.detect, channels='RGB', caption="Captured Image")
except AttributeError:
    st.error("Press the start button first")

save = st.button("Save Image")

try:
    if save:
        with tempfile.TemporaryFile() as temp_dir:
            temp_file = os.path.join(temp_dir, "captured_image.jpg")
            if st.session_state.detect.any():
                cv2.imwrite(temp_file, st.session_state.detect)
            else:
                raise KeyError("Click Start Button")
            st.success(f"Image saved Succcesfully:",{temp_file})
except KeyError:
    st.error("No Captured Image to Save")