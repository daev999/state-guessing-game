import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

user_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while True:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")

    if answer_state:   # ← safety check
        user_answer = answer_state.title()

        if user_answer in states:
            print("Correct")
        





