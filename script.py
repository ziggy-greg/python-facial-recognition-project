import cv2

def detect_face(vid_capture, scaleFactor, minNeighbors, colors):

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    ret, frame = vid_capture.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(frame, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

    for (w, x, y, z) in faces:
        cv2.rectangle(frame, (w, x), (w+y,x+z), colors, 2)
    return frame    


def hex_to_rgb(hex_color):

   hex_color = hex_color.lstrip('#')

   rgb_color = tuple(int(hex_color[i:i+2],16) for i in (0, 2,4))

   return rgb_color