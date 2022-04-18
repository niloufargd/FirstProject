# FirstProject


> This project is called Rock Paper Scissors and as the name suggests it's about playing RPS against the computer but with a twist. Instead of the usual typing method to make your choice, you literally show it to the camera. The project is built with the help of three packages: Tensorflow, opencv and ipykernel.

## Milestone 1

- First I created the model. By going to the https://teachablemachine.withgoogle.com/ . The model is made up of 4 classes: Rock, Paper, Scissors and Nothing. I took about 500 images of myself showing each gesture (and did nothing, just my face for the last one) to the camera and then trained the model (well the website itself did the hard job). Then I downloaded the model as a h5 file.
  
```python
"""Insert your code here"""
```

> Insert an image/s<img width="1316" alt="2" src="https://user-images.githubusercontent.com/44573189/163809510-bfbab29c-08e0-4165-9217-c03dd70c3d3c.png">
creenshot of what you have built so far here.

## Milestone 2


- Then I installed opencv-python, tensorflow, and ipykernel via conda terminal for a new envirenment. 

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```


```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n: Designing the logic of the game


- First the computer needs to randomley choose an option (R, P, S). First we need to import the random module. Then we define a variable called Play, then make a list of the optinos we have and then randomely choose one of them. It can be done in many ways. I write here two ways it can be done:

CODE

-Also we need to translate the prediction? we get from the computer to the actual choices. We get 4 probabbilities based on our four classes. Based on that we can define each choice of the computer. We can say any probablity higher than 0.5 means that, that particular class has been chosen. The first set of numbers we get correspond to our first class which is Rock and then Paper, Scissors and finally Nothing.

-Now we need to figure out who won. For this we need to write down the rules and code based on that.

PICTURE OF RULES

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

