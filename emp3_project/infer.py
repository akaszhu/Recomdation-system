import cv2
import numpy as np
import mediapipe as mp
import streamlit as st
from keras.models import load_model
import webbrowser

#st.image("download.jpg")
X = []
data_size = 0
model = load_model("model.h5")
label = np.load("labels.npy")

########################################################

###########################################################

st.image("download.jpg")
st.title("EMOTION BASED MUSIC RECOMMENDATION")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Choose your preffered language")
#lang = st.radio("", ['English', 'Tamil'])
lang=st.selectbox(' ',['None','English','Tamil'])
st.write("")
st.write("You have choosed ",lang)
st.image("music-kids-2155774.jpg")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
emotion = "Your emotion is not detected"
if lang== "English" or lang=="Tamil":
	while True:
		lst = []

		_, frm = cap.read()

		frm = cv2.flip(frm, 1)

		res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

		if res.face_landmarks:
			for i in res.face_landmarks.landmark:
				lst.append(i.x - res.face_landmarks.landmark[1].x)
				lst.append(i.y - res.face_landmarks.landmark[1].y)

			if res.left_hand_landmarks:
				for i in res.left_hand_landmarks.landmark:
					lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			if res.right_hand_landmarks:
				for i in res.right_hand_landmarks.landmark:
					lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
					lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			lst = np.array(lst).reshape(1, -1)

			pred = label[np.argmax(model.predict(lst))]

			print(pred)
			cv2.putText(frm, pred, (50, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
			emotion = pred
			X.append(lst)
			data_size = data_size + 1

		# drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
		# drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
		# drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

		cv2.imshow("window", frm)

		if cv2.waitKey(1) == 27 or data_size > 25:
			cv2.destroyAllWindows()
			cap.release()
			break

print(emotion)
st.write("Your emotion is captured as", emotion)
if lang == "English":
    if emotion == "Sad":
        url = 'https://open.spotify.com/playlist/5lJUNGV1DddWQu3ekPJJYB?si=qCfRKWHZT5aOGlsh0hnjnw'
        webbrowser.open_new_tab(url)
    elif emotion == "Happy":
        url = 'https://open.spotify.com/playlist/6T7OsjsasaIKr4OzBa972w?si=oH9fa8hcS9KBAir_Ro30Ug'
        webbrowser.open_new_tab(url)
elif lang == "Tamil":
    if emotion == "Sad":
        url = 'https://open.spotify.com/playlist/0DBRBO7Sls2nLpTvXcOqnU?si=hq01BTSKTv6DqK9vomoYeg'
        webbrowser.open_new_tab(url)
    elif emotion == "Happy":
        url = 'https://open.spotify.com/playlist/17n06OS3WUe5WJoNcuJCh2?si=hX2IvDqKT62_xXQmHAcyCQ'
        webbrowser.open_new_tab(url)
