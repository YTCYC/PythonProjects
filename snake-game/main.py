from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)


ytc = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(ytc.up, "Up")
my_screen.onkey(ytc.left, "Left")
my_screen.onkey(ytc.right, "Right")
my_screen.onkey(ytc.down, "Down")

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    ytc.move_snake()

    # detect eat food
    if ytc.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        ytc.extend_body()

    # detect hit wall
    # if round(ytc.head.xcor(), 0) > 280 or round(ytc.head.xcor(), 0) < -280 or round(ytc.head.ycor(), 0) > 280 or round(ytc.head.ycor(), 0) < -280:
    if round(ytc.head.xcor(), 0) > 280 or ytc.head.xcor() < -280 or round(ytc.head.ycor(), 0) > 280 or round(ytc.head.ycor(), 0) < -280:
        game_on = False
        print((ytc.head.xcor(), ytc.head.ycor()))
        scoreboard.game_over()
        print("ytc died because of hitting the wall")

    new_seg = ytc.segment[1:]
    for seg in new_seg:
        if ytc.head.distance(seg) < ytc.body_len / 2:
            print((ytc.head.xcor(), ytc.head.ycor()))
            print((seg.xcor(), seg.ycor()))
            print(ytc.head.distance(seg))
            game_on = False
            scoreboard.game_over()
            print("ytc died because of eating herself")

# ytc = []
# for position in starting_x:
#     turtle = Turtle(shape="square")
#     turtle.penup()
#     turtle.color("white")
#     turtle.goto(position, 0)
#     ytc.append(turtle)

# game_on = True
# while game_on:
#     my_screen.update()
#     time.sleep(0.1)
#     for ytc_num in range(len(ytc)-1, 0, -1):
#         ytc[ytc_num].goto(ytc[ytc_num-1].xcor(), ytc[ytc_num-1].ycor())
#     ytc[0].left(20)





# my_screen.update()






my_screen.exitonclick()
