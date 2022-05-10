from turtle import Turtle, position

class Snake():

  def __init__(self):
    # Precalculated starting Positions
    # Step Length
    self.starting_positions  = [(0 ,0), (-20, 0), (-40, 0)]
    self.step_length = 20
    self.snake_body = []
    self.create_snake()


  def new_game(self):
    for segment in self.snake_body:
      segment.reset()
      segment.clear()
    # Call the Init function to reset the snake
    self.__init__()


  def create_snake(self):
    for pos in self.starting_positions:
      self.add_segment(pos)


  def add_segment(self, pos):
    snake_segment = Turtle('square')
    snake_segment.penup()
    snake_segment.color('white')
    snake_segment.goto(pos)
    self.snake_body.append(snake_segment)


  def extend(self):
    self.add_segment(self.snake_body[-1].position())


  def move(self):
    for i in range(len(self.snake_body) - 1, 0, -1):
      x = self.snake_body[i - 1].xcor()
      y = self.snake_body[i - 1].ycor()
      self.snake_body[i].goto(x, y)
    self.snake_body[0].forward(self.step_length)


  def turn_left(self):
    if self.snake_body[0].heading() != 0:
      self.snake_body[0].setheading(180)    


  def turn_right(self):
    if self.snake_body[0].heading() != 180:
      self.snake_body[0].setheading(0)


  def turn_up(self):
    if self.snake_body[0].heading() != 270:
      self.snake_body[0].setheading(90)


  def turn_down(self):
    if self.snake_body[0].heading() != 90:
      self.snake_body[0].setheading(270)

