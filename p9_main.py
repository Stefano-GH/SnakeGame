from turtle import Screen
from p9_snake import Snake
from p9_food import Food
from p9_scoreboard import Scoreboard
import time


# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


# Move and control the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="space", fun=snake.game_off)


# Play the game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collision from the wall
    if not abs(snake.head.xcor()) < 290 or not abs(snake.head.ycor()) < 300:
        scoreboard.reset()
        snake.reset()
    
    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
    # Stop the game
    if not snake.game_on:
        game_on = False
        scoreboard.game_over()


screen.exitonclick()