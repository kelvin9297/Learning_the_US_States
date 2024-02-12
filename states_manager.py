from turtle import Turtle

FONT = ("Arial", 8, "normal")


class StatesManager:

    def __init__(self):
        self.on_screen_states = []
        self.guessed_states = []

    def appear(self, position, states):
        states_name = Turtle()
        states_name.hideturtle()
        states_name.penup()
        states_name.color("black")
        states_name.goto(position)
        states_name.write(f"{states}", align="center", font=FONT)
        self.on_screen_states.append(states_name)
        self.guessed_states.append(states)

    def score(self):
        score = len(self.on_screen_states)
        return score
