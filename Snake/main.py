from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard=Scoreboard()
snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor()> 290 or snake.head.xcor() <-290 or snake.head.ycor()> 290 or snake.head.ycor() <-290:
       scoreboard.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()


screen.exitonclick()