from turtle import Turtle,Screen
import random
is_rance_on = False
screen = Screen()
screen.setup(width=500,height = 600)
user_bet = screen.textinput(title = "Make your bet",  prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]

all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[i])
    m = -200
    new_turtle.penup()
    new_turtle.goto(x = -230, y =m + (i * 70))
    all_turtles.append(new_turtle)
if user_bet:
    is_rance_on = True

while is_rance_on:

    for turtles in all_turtles:
        if turtles.xcor() >230:
            is_rance_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        turtles.forward(random.randint(0, 10))
# for i in range(6):
#     tim = Turtle(shape="turtle")
#     tim.

# tim = Turtle(shape="turtle")
# jim = Turtle(shape="turtle")
# sam = Turtle(shape="turtle")
#
# tim.goto(x=-230,y=-100)
# tim.penup()
# jim.goto(x=-230,y = 0)

screen.exitonclick()