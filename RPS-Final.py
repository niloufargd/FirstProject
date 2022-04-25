import random
import time
import cv2
from keras.models import load_model
import numpy as np

model = load_model(r'C:\Users\nilou\Desktop\AiCore\New model\converted_keras\keras_model.h5')
cap = cv2.VideoCapture(0)
start_time = time.time()
text = ''
text_2 = ''
text_3 = ''
text_4 = ''
switch = True
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
rounds = 1
user_count = 0
ai_count = 0
user_choice = 0
ai_choice = 0

def camera():
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


def beginning():
    global text_4
    global switch
    print("good")
    text_4 = "Press P to play!"
    if cv2.waitKey(33) & 0xFF == ord('p'):
        text_4 = ''
        switch = False
        count_down()

def press_continue():
    global text_4
    global switch
    text_4 = "Press C to continue to the next round"
    if cv2.waitKey(33) & 0xFF == ord('c'):
        text_4 = ''
        switch = False
        count_down()


def play():
    print("play")
    global switch
    global user_choice
    global ai_choice
    prediction = model.predict(data)
    pool_choices = ["rock", "paper", "scissors"]
    random_index = random.randint(0, 2)
    ai_choice = pool_choices[random_index]

    if prediction[0][0] > 0.5:
        user_choice = "rock"

    elif prediction[0][1] > 0.5:
        user_choice = "paper"

    elif prediction[0][2] > 0.5:
        user_choice = "scissors"

    else:
        user_choice = "nothing"

    if user_choice == ai_choice:
        return (0, user_choice, ai_choice)

    if helper(user_choice, ai_choice):
        return (1, user_choice, ai_choice)

    else:
        return (-1, user_choice, ai_choice)


def helper(human, robot):
    if (human == "rock" and robot == "scissors") or (human == "scissors" and robot == "paper") or (
            human == "paper" and robot == "rock"):
        return True
    return False

def count_down():
    global text
    global text_2
    global text_3
    global text_4
    global switch
    if switch == False:
        t = (7 * rounds) - (time.time() - start_time)
        text_2 = ''
        text_3 = ''
        text_4 = ''
        text = f'Be ready in {int(t)} seconds'
        print(t)
        if t <= 0:
            text = ''
            switch = True
            winner()


def winner():
    global switch
    global text
    global ai_count
    global user_count
    global user_choice
    global ai_choice
    global rounds
    global text_2
    global text_3
    global text_4
    result, user_choice, ai_choice = play()

    if result == 0:
        rounds += 1
        print(user_count)
        print(ai_count)
        text =f'You both have chosen {user_choice}!'
        text_2 = ''
        text_3 = ''
        text_4 = ''


    elif result == 1:
        rounds += 1
        user_count += 1
        print(user_count)
        print(ai_count)
        text = f'You have chosen {user_choice}'
        text_2 = f'The computer has chosen {ai_choice}'
        text_3 = 'You won this round!'


    else:
        rounds += 1
        ai_count += 1
        print(user_count)
        print(ai_count)
        text = f'You have chosen {user_choice}'
        text_2 = f'The computer has chosen {ai_choice}'
        text_3 = 'Damn, You lost this round!'



def finish():
    global text_4
    global text_3
    text_4 = 'Press q to Quit'
    if user_count > ai_count:
        text_3 = 'Yaay! You won the game!'

    elif user_count < ai_count:
        text_3 = "Oh no... You've lost the game!"
    elif user_count == ai_count:
        text_3 = "Boring...It's a draw!"

def main():
    global rounds
    while rounds < 7:
        camera()
        checkpoint()
        count_down()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


main()
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
