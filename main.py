from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
# Global variable is_game_on
is_game_on = True

snake = Snake()
food = Food()
score = Scoreboard()


screen = Screen()
screen.setup(600, 480)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


def main_loop():
  global is_game_on
  while is_game_on:
    # Different Dificulty Levels
    if score.score < 10:
      time.sleep(0.15)
    elif score.score < 20:
      time.sleep(0.13)
    elif score.score < 30:
      time.sleep(0.11)
    elif score.score < 40:
      time.sleep(0.09)
    elif score.score < 50:
      time.sleep(0.07)
    elif score.score < 60:
      time.sleep(0.05)
    else:
      time.sleep(0.03)

    screen.update()
    snake.move()

    # Collision with food
    if snake.snake_body[0].distance(food) < 15:
      
      # print(snake.snake_body[0].heading())
      food.new_position()
      score.update_score()
      snake.extend()

    # Collision with Walls
    if snake.snake_body[0].xcor() > 300 or snake.snake_body[0].xcor() < -300:
      is_game_on = False
      score.game_over()
    elif snake.snake_body[0].ycor() > 260 or snake.snake_body[0].ycor() < -260:
      is_game_on = False
      score.game_over()

    # Collision with Tail
    for body in snake.snake_body[1:]:
      if snake.snake_body[0].distance(body) < 10:
        is_game_on = False
        score.game_over()


def new_game():
  global is_game_on
  is_game_on = True
  score.clear_score()
  snake.new_game()
  food.new_position()
  main_loop()


screen.listen()

screen.onkeypress(snake.turn_left, key='Left')
screen.onkeypress(snake.turn_right, key='Right')
screen.onkeypress(snake.turn_up, key='Up')
screen.onkeypress(snake.turn_down, key='Down')
screen.onkeypress(new_game, key='Return')

main_loop()

screen.exitonclick()