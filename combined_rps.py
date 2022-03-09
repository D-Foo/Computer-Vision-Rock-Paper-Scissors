import rps_game
import cv2
from keras.models import load_model
import numpy as np
import time

choice_list = ["rock", "paper", "scissors"]
my_rps_game = rps_game.Rps(choice_list)
model = load_model('RPS_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def parse_model_output(prediction):
    #Find largest index in model output and map it to choice list(appended with "nothing")
    prediction_list = prediction.tolist()[0]
    largest_index = prediction_list.index(max(prediction_list))
    output_list = choice_list
    output_list.append("no choice")
    print("You chose " + output_list[largest_index])
    return


#Main Loop
while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    #Wait for input for game start/exit program

    #Start 3s countdown 

    #Read webcam input

    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)

    #Get output from model

    #Calculate game outcome
    parse_model_output(prediction)

    #Output outcome to user

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        pass#Start game countdown

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()