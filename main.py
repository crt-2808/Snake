from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import Scoreboard


screen=Screen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game_in_on=True
screen.listen()
screen.onkey(snake.moveUp, "w")
screen.onkey(snake.moveDown, "s")
screen.onkey(snake.moveLeft, "a")
screen.onkey(snake.moveRight, "d")



while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.addScore()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.xcor()<-280:
        game_in_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_in_on=False
            scoreboard.game_over()

screen.exitonclick()
