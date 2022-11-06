from turtle import Turtle, Screen
import random


def race():
    turtles =[]
    screen = Screen()
    screen.setup(500,400)
    user_bet=screen.textinput(title="Make your bet", prompt= "Wich turtle will win the race? Enter a color: ")
    colors=["red","orange", "yellow", "green", "blue", "purple"]
    is_race_on=False
    start_x = (screen.window_width() / 2) * (-1) + 50
    start_y = (screen.window_height() / 2) - 50
    for i in range(len(colors)):
        new_turtle=Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(start_x, start_y)
        start_y -= 50
        turtles.append(new_turtle)
        xcor_of_finish_line=(screen.window_width())/2-20

    if user_bet:
        is_race_on=True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor()>xcor_of_finish_line:

                winning_color= turtle.pencolor()
                if winning_color==user_bet:
                    print(f"You have won! {winning_color} turtle is winner!")
                else:
                    print(f"You have lost! {winning_color} turtle is winner!")
                is_race_on=False

            rand_distance=random.randint(0,10)
            turtle.forward(rand_distance)


    screen.exitonclick()



def main():
    race ()

if __name__ == "__main__":
    main()