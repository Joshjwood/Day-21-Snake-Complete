from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake 2021")
screen.tracer(0)



#starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#create snake
#segments = []

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.level_up()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        snake.reset()

        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.reset()

            scoreboard.reset()

screen.exitonclick()
