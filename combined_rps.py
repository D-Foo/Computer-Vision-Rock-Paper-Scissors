import rps_game
import cv2
from keras.models import load_model
import numpy as np
import time

#Function Defs
def parse_model_output(prediction):
    #Find largest index in model output and map it to choice list(appended with "nothing")
    prediction_list = prediction.tolist()[0]
    largest_index = prediction_list.index(max(prediction_list))
    output_list = choice_list[:]
    output_list.append("no choice")
    print("You chose " + output_list[largest_index])
    return output_list[largest_index]

def render_text(text_str, frame):
    x = 540
    y = 40
    color = (255, 255, 255)
    cv2.putText(frame, text_str, (x, y), 0, 1, color, 1, cv2.LINE_AA)



#Variables
choice_list = ["rock", "paper", "scissors"]
my_rps_game = rps_game.Rps(choice_list)
model = load_model('RPS_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
game_ongoing = False
rps_countdown = 3.0 #How long to wait before getting user input
render_text_str = ""
game_count = 0
score_victory_condition = 3

#Main Loop
while True:  

    #Wait for input for game start/exit program
    if(game_ongoing):
        #Start 3s countdown 
        time_diff = time.time() - game_start_time
        if(time_diff >= rps_countdown):
            game_ongoing = False
        else:
            render_text_str = "{:.2f}".format(3.0 - time_diff) + "s"
    else:
        render_text_str = "Ready"

    
    #Read webcam input
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image

    #Flip input and display webcam input
    frame = cv2.flip(frame, 1)
    render_text(render_text_str, frame)
    cv2.imshow('frame', frame)    

    #Game timed
    if(game_ongoing == False):

        #Play game at end of timer
        #Get output from model
        prediction = model.predict(data)

        #Calculate game outcome and output
        my_rps_game.play_with_camera_input((parse_model_output(prediction)))

        #Increase game count
        game_count += 1
        if(my_rps_game.player_score >= score_victory_condition or my_rps_game.computer_score >= score_victory_condition):
            break

        #Start new game
        game_ongoing = True
        game_start_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    
#Output Score
my_rps_game.output_score()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()