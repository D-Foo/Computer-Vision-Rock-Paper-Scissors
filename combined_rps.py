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
    output_list = choice_list[:]
    output_list.append("no choice")
    print("You chose " + output_list[largest_index])
    return output_list[largest_index]

def render_text(rps_timer, frame):
    text_str = ""
    x = 200
    y = 60
    color = (255, 255, 255)
    if(rps_timer):
        text_str = str(rps_timer)
    else:
        text_str = "Ready"
    cv2.putText(frame, text_str, (x, y), 0, 1, color, 1, cv2.LINE_AA)

#Main Loop
while True: 
    game_start = False
    rps_countdown = 3.0 #How long to wait before getting user input
    rps_timer = 0.0     #Timer to track 
    
    #Wait for input for game start/exit program
    if(game_start):
        #Start 3s countdown 
        rps_timer = rps_countdown
        game_start = False
 
    #Read webcam input
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image

    #Flip input and display webcam input
    frame = cv2.flip(frame, 1)
    render_text(rps_timer, frame)
    cv2.imshow('frame', frame)

    #Get output from model
    prediction = model.predict(data)

    #Calculate game outcome
    my_rps_game.play_with_predetermined_input((parse_model_output(prediction)))

    #Output outcome to user

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        game_start
        pass#Start game countdown

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()