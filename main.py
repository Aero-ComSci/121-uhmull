import turtle
import random

spot_color = "pink"
spot_radius = 15  
timer = 30 #seconds
counter_interval = 1000
timer_up = False
colors = ['pink', 'purple', 'green', 'red', 'blue', 'orange']
sizes = [0.5, 1, 1.5, 1.75, 2, 2.25]
score = 0
screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.bgcolor("plum")
spot = turtle.Turtle()
spot.shape("circle") 
spot.fillcolor(spot_color)
spot.penup()

def spot_clicked(x, y):
    global timer_up, spot_radius
    if not timer_up:
      spot_color = random.choice(colors)
      spot.fillcolor(spot_color)
      spot.penup()
      spot.hideturtle()
      spot.goto(random.randint(-100, 100), random.randint(-100, 100))
      spot_radius = random.choice(sizes) * 8
      spot.showturtle()
      update_score()
      
def update_score():
    global score
    score += 1
    print("Score:" + str(score))
    
spot.onclick(spot_clicked)
update_score()
screen.mainloop()
