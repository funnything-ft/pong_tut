from turtle import Turtle

class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape('circle')
    self.color('blue')
    self.goto(0, 0)
    self.shapesize(stretch_len=1, stretch_wid=1)
    self.direction_y = 1
    self.direction_x = 1
    self.move_speed = 0.1
    
  def move(self):
    new_x = self.xcor() + 10 * self.direction_x
    new_y = self.ycor() + 10 * self.direction_y
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.direction_y *= -1
    
  def bounce_x(self):
    self.direction_x *= -1
    self.move_speed *= 0.9
    
  def reset(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.bounce_x()
    