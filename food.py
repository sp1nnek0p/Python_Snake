from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.colors_list = ['red', 'maroon', 'purple', 'cyan', 'gold', 'yellowgreen']
    self._create_food()
    self.new_position()
    

  def _create_food(self):
    self.shape('square')
    self.penup()
    self.color(random.choice(self.colors_list))
    self.speed('fastest')
  

  def _rand_height(self):
    return int(random.randrange(-220, 220,20))


  def _rand_width(self):
    return int(random.randrange(-280, 280, 20))


  def new_position(self):
    self.color(random.choice(self.colors_list))
    self.goto(x=self._rand_width(), y=self._rand_height())