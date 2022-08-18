from turtle import Screen
from food import Food
import time
from snake import Snake
from score import Score
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
snake = Snake()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True

food = Food()
score = Score()
while game_on:
    screen.update()
    time.sleep(.1)
    snake.Move()
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        score.update()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300 :
        snake.reset()
        score.game_repeat()


    for i in snake.list1[1:]:
        if snake.head.distance(i) < 10:
            score.game_repeat()
            snake.reset()
            # score.write(arg="Game Over !!", align="center", font=("courier", 24, "normal"))

screen.exitonclick()
