from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.color('white')
      self.penup()
      self.hideturtle()
      self.goto(0, 210)
      self.score = 0
      self.write_score()from turtle import Turtle
from highscore import Highscore

class Scoreboard(Turtle):
  def __init__(self) -> None:
      super().__init__()
      self.highscore = Highscore()
      self.color('white')
      self.penup()
      self.hideturtle()
      self.goto(0, 210)
      self.score = 0
      self.write_score()


  def update_score(self):
    self.score += 1
    self.write_score()


  def write_score(self):
    self.clear()
    self.write(f'Score: {self.score} | Highscore: {self.highscore.get_highscore()}', align='center', font=('OCR A Extended', 20, 'normal'))
  

  def game_over(self):
    self.goto(0, 0)
    self.color('red')
    self.write('GAME OVER', align='center', font=('OCR A Extended', 46, 'bold'))
    self.goto(0, -50)
    self.write('Press ENTER to Play again', align='center', font=('OCR A Extended', 16, 'normal'))

    if self.score > int(self.highscore.get_highscore()):
      self.highscore.set_highscore(self.score)

  def clear_score(self):
    self.clear()
    self.__init__()


  def update_score(self):
    self.score += 1
    self.write_score()


  def write_score(self):
    self.clear()
    self.write(f'Score: {self.score}', align='center', font=('OCR A Extended', 20, 'normal'))
  

  def game_over(self):
    self.goto(0, 0)
    self.color('red')
    self.write('GAME OVER', align='center', font=('OCR A Extended', 46, 'bold'))
    self.goto(0, -50)
    self.write('Press ENTER to Play again', align='center', font=('OCR A Extended', 16, 'normal'))


  def clear_score(self):
    self.clear()
    self.__init__()
