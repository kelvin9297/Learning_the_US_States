import turtle
import pandas
from states_manager import StatesManager

screen = turtle.Screen()
states_manager = StatesManager()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_state_list = data["state"].to_list()

game_is_on = True
while states_manager.score() < 50:
    answer_state = screen.textinput(title=f"{states_manager.score()}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_state_list if state not in states_manager.guessed_states]

        # missing_states = []
        # for state in all_state_list:
        #     if state not in states_manager.guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state_list and answer_state not in states_manager.guessed_states:
        state_cor = data[data.state == answer_state]
        x_cor = state_cor.x
        y_cor = state_cor.y
        position = (int(x_cor), int(y_cor))
        states_manager.appear(position, answer_state)
