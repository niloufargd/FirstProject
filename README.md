# FirstProject


> This project is called Rock Paper Scissors and as the name suggests it's about playing RPS against the computer but with a twist. Instead of the usual typing method to make your choice, you literally show it to the camera. The project is built with the help of three packages: Tensorflow, opencv and ipykernel.

## Milestone 1

- First I created the model. By going to the https://teachablemachine.withgoogle.com/ . The model is made up of 4 classes: Rock, Paper, Scissors and Nothing. I took about 500 images of myself showing each gesture (and did nothing, just my face for the last one) to the camera and then trained the model (well the website itself did the hard job). Then I downloaded the model as a h5 file called keras_model.h5 .
  

<img width="1316" alt="2" src="https://user-images.githubusercontent.com/44573189/163809510-bfbab29c-08e0-4165-9217-c03dd70c3d3c.png">


## Milestone 2


- Then I installed opencv-python, tensorflow, and ipykernel via Anaconda terminal for a new envirenment called my_env. I use PyCharm as my IDE.
- Afterwards I downloaded the file that AiCore gave us to run the project. I changed the path for the model and entered the path where I have saved my trained model.
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

## Milestone 3: Designing the logic of the game


- First the computer needs to randomley choose an option (R, P, S). For that to happen, we need to import the random module. Then we define a variable called Play, then make a list of the options we have and then randomely choose one of them. It can be done in many ways. I write here two ways it can be done:
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
-Also we need to translate the prediction we get from the computer to the actual choices. We get 4 probabilities based on our four classes. Based on that we can define each choice of the computer. We can say any probablity higher than 0.5 means that, that particular class has been chosen. The first set of numbers we get correspond to our first class which is Rock and then Paper, Scissors and finally Nothing.
```

if prediction[0][0] > 0.5:
            user_choice = "rock"

        elif prediction[0][1] > 0.5:
            user_choice = "paper"

        elif prediction[0][2] > 0.5:
            user_choice = "scissors"

        else:
            user_choice = "nothing
```
-Now we need to figure out who won. For this we need to write down the rules and code based on that.

![Game-tree-for-one-round-of-Rock-Paper-and-Scisors-In-the-first-column-are-the](https://user-images.githubusercontent.com/44573189/163812664-e11130c7-0668-43d1-bb13-b0ab895e802b.png)


-Okay then now first thing we is to get rid of the easiest option which is when there's a tie.

```

        if user_choice == ai_choice:
            return "It's a tie!"
```

-Then we take care of the times when the use has won and computer last. For this we can use a helper function. Inside the function we define a condition which includes all the times we/user wins and the computer loses and returns True, otherwise it returns False.

```

    def helper (human, robot):
        if (human == "rock" and robot == "scissors") or (human == "scissors" and robot == "paper") or (human == "paper" and robot == "rock"):
            return True
        return False
```
-And now what remains is the time computer has won.

-Now we have to keep track of who has won to have an ultimate winner. When there's a tie, we don't add any points to anyone. And when either one wins we add one point. Anyone who has won 3times will be the ultimate winner.

-We define a function for that. And before that for the 3 possible scenarios we make it return 0 for when there's a tie, 1 for when the user wins and -1 for when the computer wins also we return the variable for the computer's choice and the user's choice along with it so that we can print it later in the other funstion. 

```
        if user_choice == ai_choice:
            return (0, user_choice, ai_choice)

        if helper(z, ai_choice):
            return (1, user_choice, ai_choice)

        return (-1, user_choice, ai_choice)
  ```      

-We define two variables inside this new function one to keep track of each win of the user and the other one to keep track of the wins of computer. 

```
    def winner():
        user_count = 0
        ai_count = 0
        
```
-Then we define a condition, whenever either computer or the user wins three times print You have won or You have lost, otherwise keep playing by going to the Play function and also we set three variables result, user choice and computer choice so to the three values it returns. 

```
    def winner():
        user_count = 0
        ai_count = 0
        while user_count < 3 and ai_count < 3:
            result, user_choice, ai_choice = play()
           #tie
            if result == 0:
                print("You both have chosen {}.\n".format(user_choice))

            elif result ==1:
                user_count += 1
                print("You have chosen {} and the computer has chosen {}. You won!\n".format(user_choice, ai_choice))
            else:
                ai_count += 1
                print("You have chosen {} and the computer has chosen {}. You lost!. \n".format(zuser_choice, ai_choice))
            print("\n")

        if user_count > ai_count:
            print("You have won 3 rounds!")
        else:
            print("You have lost 3 rounds!")
```
# Milestone 4

COUNTDOWN TIMER: To have a wokring countdowntimer in our project we need to import the time module. Then we define a function and call it count_down_time and give it a t as a parametre. Then inside the function we set t to the secs variable and then using the python formating to show timer and print it, we also set the sleep time to 1 second and then decrement t one at a time. 

```
    def count_down_time(t):
        while t:
            secs = t
            timer = '{:02d}'.format(secs)
            print(timer)
            time.sleep(1)
            t -= 1
 ```         

- But then you will find out that since we're using the camera, nothing should interefere with the main while loop. That means time.sleep() and another while loop can not be used.

-So instead for a timer we need a funstion that is updated every second. We use time.time() method which gives us a floating number expressed in seconds since the epoch, in UTC. Epoch is a fixed time. 

-There is formula for finding out the elapsed time to see how much time the program takes to do a task. We can use this to our benefit by first defining start-time as time.time() which gives us the static epoch time and then using the actual method in the program to get a changing number.

-For the program to work we need to close circuit and keep the ball rolling in one corner. Which means having on and off switches by the help of boolean expressions. We need 3 function in the program that should be kept checked. We keep those in the main while loop and others out.

-The first important function is the one which has all the data for the the camera to work.

```
def camera():
    global text
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    logo = cv2.imread(r'C:\Users\nilou\Desktop\AiCore\Batman.png')
    size = 100
    logo = cv2.resize(logo, (size, size))
    img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    roi = frame[-size - 10:-10, -size - 10:-10]
    roi[np.where(mask)] = 0
    roi += logo
    cv2.putText(frame, 'RPS Game', (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (120, 0, 0), 2)
    cv2.putText(frame, text, (10, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (86, 116, 185), 2)
    cv2.putText(frame, text_2, (10, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (86, 116, 185), 2)
    cv2.putText(frame, text_3, (10, 300), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 120, 0), 2)
    cv2.putText(frame, text_4, (10, 400), cv2.FONT_HERSHEY_TRIPLEX, 1, (120, 0, 0), 3)
    cv2.imshow('frame', frame)

```

-The second one is about a function we define to keep track of the game and call it check point. 

```
def checkpoint():
    global switch
    if switch == True:
        if rounds == 1:
            beginning()

        elif rounds == 6:
            print("last round")
            finish()

        elif rounds >= 1:
            print("continue")
            print(f"rounds are {rounds}")
            press_continue()
```

-The third one that we will need to keep the loop going inside it at some point is the function we define for countdown.

```
def count_down():
    global text
    global countdown
    global text_2
    global text_3
    global text_4
    global switch
    global game_play
    global check_point
    if switch == False:
        t = (7 * rounds) - (time.time() - start_time)
        if countdown == True:
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text = f'Be ready in {int(t)} seconds'
            print(t)
        if t <= 0:
            text = ''
            switch = True
            countdown = False
            winner()
```

## Problems and how to deal with them:

-First variables have scope in python. A variable defined outside a function can be accessed inside the function but can not be altered. if we want to alter it we need to call them inside the function like this: global var.

Also for the game to work, we need to keep track of how many rounds we have played. We can create a variable called round and add to it every time the game is played.

```
    if result == 0:
        rounds += 1

    elif result == 1:
        rounds += 1
        user_count += 1


    else:
        rounds += 1
        ai_count += 1

```

 So another problem that need to be dealt with is the countdown, it works fine for the first time if we substitute the result of time.time - start_time from a fixed number like 7. But for other times it won't work because t is already < 0. We need to have that fixed number combined with a variable that is updated throughout the game. We can either use rounds or the result of either ai or user. But the latter won't work because either could win or lose so it won't change for sure each time. So we use rounds.

Also, the result should be converted to an integer to be shown on the camera.

Also because we are using the round variable from the start in our countdown, it can't be zero. We start from 1.

We define a boolean to keep the pots closed. We call it switch. Whenever the switch is on (True), the lid of the checkpoint is open and whenever the switch is off (False), the countdown works. 

For text issue, we can go and check this out. I used different colors and I also added a batman logo to my game. 




![Batman](https://user-images.githubusercontent.com/44573189/165062817-e036ad32-1fa2-4d89-a72c-e22fe8ab7f02.png)

