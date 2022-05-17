class Highscore:

  def __init__(self):
    pass

  def get_highscore(self):
    try:
      with open('highscore.txt' , 'r') as rfile:
        self.highscore = rfile.read()
    except:
      with open('highscore.txt', 'w') as wfile:
        wfile.write('0')
        self.highscore = '0'
    return self.highscore


  def set_highscore(self, new_highscore = 0):
    with open('highscore.txt', 'w') as file:
      file.write(str(new_highscore))