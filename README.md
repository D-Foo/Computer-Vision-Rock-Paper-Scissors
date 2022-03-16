# Rock Paper Scissors with Webcam Input

A small project exploring the possible applications of Google's [Teachable Machine](https://teachablemachine.withgoogle.com/) by combining it with a rock paper scissors game written while learning python.
 
> Made with [TensorFlow](https://www.tensorflow.org/learn) and [OpenCv](https://pypi.org/project/opencv-python/)

## Creating the Model

Created a model using Teachable Machine by posing in front of the camera in rock paper scissors poses and a neutral pose for an option for no input.

## Setting up the environment

Created a conda environment for the project then downloaded and installed TensorFlow and OpenCv libraries. 

```bash
conda create --name tensorflow-env
conda activate tensorflow-env
conda install tensorflow
conda install opencv
```

TensorFlow is used to load and interface with the model made from Teachable Machine

```python
from keras.models import load_model
model = load_model('RPS_MODEL.h5')
```

## Creating a Rock Paper Scissors Game with Python

I was familiar with writing code in C++ from my time at university so it was interesting to write a game in python along with it being a great way to familiarise myself with the language. While writing it I could see why python is chosen for rapid development and prototyping over other languages.


## Putting it all together

All the different aspects of the project need to be included together, to do that we combine the camera, Teachable Machine model and rock, paper, scissors game code together in a while true loop.

- Get camera input and pass to ml model
```python
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
```

- Get model output and parse then pass to RPS game logic

  The model outputs a numpy 1D array which is first converted to a list, then mapped to an array of possible inputs, before being passed to the rock, paper, scissors game.
```python
  def parse_model_output(prediction):
      #Find largest index in model output and map it to choice list(appended with "no choice")
      prediction_list = prediction.tolist()[0]
      largest_index = prediction_list.index(max(prediction_list))
      output_list = choice_list[:]
      output_list.append("no choice")
      print("You chose " + output_list[largest_index])
      return output_list[largest_index]
      
  prediction = model.predict(data)
  my_rps_game.play_with_camera_input((parse_model_output(prediction)))
  ```

- Output countdown text to the top left of the screen so the user can simulate rock, paper, scissors.
```python
	def render_text(text_str, frame):
	    x = 540
	    y = 40
	    color = (255, 255, 255)
	    cv2.putText(frame, text_str, (x, y), 0, 1, color, 1, cv2.LINE_AA)

	frame = cv2.flip(frame, 1)
    render_text(render_text_str, frame)
    cv2.imshow('frame', frame)    
```

- Screenshot of game working
![rps_output](https://user-images.githubusercontent.com/36233522/158681289-afef4d73-aea9-447c-8906-3001595a6f51.png)

## Conclusions

It was great to explore the potential of machine learning models by combining them with other technologies. I had a really enjoyable experience learning python and seeing how it can be used to quickly develop and work with other technologies.

The game could use better interface and output with more user control, along with a better way of simulating the computer playing so the experience feels more immersive.
