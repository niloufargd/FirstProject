# FirstProject

# Example Project Documentation Guideline

> Include here a brief description of the project, what technologies are used etc.
> This project is called Rock Paper Scissors and as the name suggests it's about playing RPS against the computer but with a twist. Instead of the usual typing method to make your choice, you literally show it to the camera. The project is built with the help of three packages: Tensorflow, opencv and ipykernel.

## Milestone 1

- Answer some of these questions in the next few bullet points. What have you built? What technologies have you used? Why have you used those?

- Example: The FastAPI framework allows for fast and easy construction of APIs and is combined with pydantic, which is used to assert the data types of all incoming data to allow for easier processing later on. The server is ran locally using uvicorn, a library for ASGI server implementation.
- First I created the model. By going to the https://teachablemachine.withgoogle.com/ . The model is made up of 4 classes: Rock, Paper, Scissors and Nothing. I took about 500 images of myself showing each gesture (and did nothing, just my face for the last one) to the camera and then trained the model (well the website itself did the hard job). Then I downloaded the model as a h5 file.
  
```python
"""Insert your code here"""
```

> Insert an image/screenshot of what you have built so far here.

## Milestone 2

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).
- Then I installed opencv-python, tensorflow, and ipykernel via conda terminal for a new envirenment. 

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n: Designing the logic of the game

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.
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

-We define a function for that. And before that for the 3 possible scenarios we TAEEN a ?? 0 for when there's a tie, 1 for when the user wins and -1 for when the computer wins. 

-We define two variables inside this new function to one to keep track of each win of the computer and the other one to keep track of the wins of user.

Then we a condition, whenever either computer or the user wins three times print You have won or You have lost, otherwise keep playing.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!
-
## Milestone n

COUNTDOWN TIMER: To have a wokring countdowntimer in our project we need to import the time module.

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.
- 

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.
- 

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.
- 

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
