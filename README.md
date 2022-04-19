# FirstProject


> This project is called Rock Paper Scissors and as the name suggests it's about playing RPS against the computer but with a twist. Instead of the usual typing method to make your choice, you literally show it to the camera. The project is built with the help of three packages: Tensorflow, opencv and ipykernel.

## Milestone 1

- First I created the model. By going to the https://teachablemachine.withgoogle.com/ . The model is made up of 4 classes: Rock, Paper, Scissors and Nothing. I took about 500 images of myself showing each gesture (and did nothing, just my face for the last one) to the camera and then trained the model (well the website itself did the hard job). Then I downloaded the model as a h5 file called keras_model.h5 .
  

> Insert an image/s<img width="1316" alt="2" src="https://user-images.githubusercontent.com/44573189/163809510-bfbab29c-08e0-4165-9217-c03dd70c3d3c.png">


## Milestone 2


- Then I installed opencv-python, tensorflow, and ipykernel via Anaconda terminal for a new envirenment called my_env. I use PyCharm as my IDE.
- Afterwards I downloaded the file that AiCore gave us to run the project. I changed the path for the model and entered the path where I have saved my trained model.
-  
- Note: I tried Spyder and VS Code but I got errors running the code. For VS Code I would get missing dll files and although I tried many solutions available on stackoverflow, I couldn't get to work and used PyCharm instead. I also installed Ubuntu and tried running that on VS Code but turns out that way it can not have access to the camera. 

- The cv2.VideoCapture(0) part of the code opens a camera for video capturing. 0 is for the default computer's camera. Also the cv2.imshow() method is used to display an image in a window. And prediction is a list containing 4 probabilities that correspond to our 4 classes.

```python
"""import cv2
from keras.models import load_model
import numpy as np
model = load_model('YOUR_MODEL.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()"""
```

> 

## Milestone n: Designing the logic of the game


- First the computer needs to randomley choose an option (R, P, S). First we need to import the random module. Then we define a variable called Play, then make a list of the options we have and then randomely choose one of them. It can be done in many ways. I write here two ways it can be done:
```
"""
pool_choices = ["rock", "paper", "scissors"]
        random_index = random.randint(0, 2)
        ai_choice = pool_choices[random_index]
```

ALso:
```

ai_choice = random.choice(["rock", "paper", "scissors"])

```
-Also we need to translate the prediction? we get from the computer to the actual choices. We get 4 probabbilities based on our four classes. Based on that we can define each choice of the computer. We can say any probablity higher than 0.5 means that, that particular class has been chosen. The first set of numbers we get correspond to our first class which is Rock and then Paper, Scissors and finally Nothing.
```

if prediction[0][0] > 0.5:
            z = "rock"

        elif prediction[0][1] > 0.5:
            z = "paper"

        elif prediction[0][2] > 0.5:
            z = "scissors"

        else:
            z = "nothing
```
-Now we need to figure out who won. For this we need to write down the rules and code based on that.

![Game-tree-for-one-round-of-Rock-Paper-and-Scisors-In-the-first-column-are-the](https://user-images.githubusercontent.com/44573189/163812664-e11130c7-0668-43d1-bb13-b0ab895e802b.png)


-Okay then now first thing we is to get rid of the easiest option which is when there's a tie.

CODE

-Then we take care of the times when the use has won and computer last. For this we can use a helper function. Inside the function we define a condition which includes all the times we/user wins and the computer loses and returns True, otherwise it returns False.

Important: The name of the variables inside each function only works when we're inside that function. Do not use repetitive names from outside the function. 

-And now what remains is the time computer has won.

-Now we have to keep track of who has won to have an ultimate winner. When there's a tie, we don't add any points to anyone. And when either one wins we add one point. Anyone who has won 3times will be the ultimate winner.

-We define a function for that. And before that for the 3 possible scenarios we make it return 0 for when there's a tie, 1 for when the user wins and -1 for when the computer wins also we return the variable for the computer's choice and the user's choice along with it so that we can print it later in the other funstion. 

-We define two variables inside this new function one to keep track of each win of the user and the other one to keep track of the wins of computer. 

-Then we define a condition, whenever either computer or the user wins three times print You have won or You have lost, otherwise keep playing by going to the Play function and also we set three variables result, user choice and computer choice so to the three values it returns. 


-
## Milestone n

COUNTDOWN TIMER: To have a wokring countdowntimer in our project we need to import the time module. Then we define a function and call it count_down_time and give it a t as a parametre. Then inside the function we set t to the secs variable an d then using the python formating to show timer and print it, we also set the sleep time to 1 second and then decrement t one at a time. 

- I added the time function to many places to make the game more user-friendly and enjoyable. The countdown shows up first when you want to play, when you finish the game and each time you want to make a choice to give you time.


## Milestone n

- 

## Milestone n

- 

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

