import turtle
import random

spot_color = "pink"
spot_radius = 15  
timer = 30 #seconds
counter_interval = 1000
timer_up = False
colors = ['pink', 'purple', 'green', 'red', 'blue', 'orange']
sizes = [0.2, 0.5, 0.8, 1, 1.3]
score = 0
screen = turtle.Screen()
screen.setup(width=300, height=300)
screen.bgcolor("plum")
spot = turtle.Turtle()
spot.shape("circle") 
spot.fillcolor(spot_color)
spot.penup()
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 500)
font_setup = ("Arial", 20, "normal") #got help with gemini to fix this line of code (it wasn't being definded before)

def spot_clicked(x, y):
    global timer_up, spot_radius
    if not timer_up:
      spot_color = random.choice(colors)
      spot.fillcolor(spot_color)
      spot.penup()
      spot.hideturtle()
      spot.goto(random.randint(-100, 100), random.randint(-100, 100))
      spot_radius = random.choice(sizes) * 20
      spot.showturtle()
      update_score()
      
def update_score():
    global score
    score += 1
    print("Score:" + str(score))
    
def update_timer():
    global timer, timer_up
    score_writer.clear()
    if timer <= 0:
        score_writer.write("Time's Up!", font=font_setup)
        timer_up = True
    else:
        score_writer.write("Time: " + str(timer) + " seconds", font=font_setup) 
        timer -= 1
        screen.ontimer(update_timer, counter_interval) 
    
spot.onclick(spot_clicked)
screen.ontimer(update_timer, counter_interval) # got help from the PLTW example
update_score()
screen.mainloop()
