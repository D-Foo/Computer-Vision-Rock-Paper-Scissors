import rps_game
import cv2
from keras.models import load_model
import numpy as np

my_rps_game = rps_game.Rps(rps_game.choice_list)
model = load_model('RPS_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
