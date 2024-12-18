# updating this code to work better but the assignment was finished on the deadline but I didn't get the chance to update it then due to missing majority of the lab days because of Tennis
import turtle as trtl
import random

#my variables
spot_color = "pink"
spot_size = int("3")
spot_shape = "circle"
totalScore = 0
font_setup = ("MonoLisa", 20)
timer = 30
counter_interval = 1000  
timer_up = False
colors = ['pink', 'purple', 'green', 'red', 'blue', 'orange']
sizes = [0.5, 1, 1.5, 1.75, 2, 2.25]

trtl = trtl.Screen()
trtl.setup(width=300, height=300)
spot = trtl
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
counter = trtl.Turtle()
trtl.bgcolor("mistyRose")

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Your time is up ):", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.hideturtle()
    score_writer.write(score, font=font_setup)
def change_position():
    new_xpos = random.randint(-200, 200)
    new_ypos = random.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)
    update_score()
def spot_clicked(x, y):
    global timer_up
    if not timer_up: 
        spot.penup()
        spot.hideturtle()
        change_position()
        spot.showturtle()
        spot.pendown()
        new_color()
        new_sizes()
def new_color(): 
    random_color = random.choice(colors)
    spot.color(random_color)
    spot.stamp()
    spot.color(spot_color)
def new_sizes(): 
    newsize = random.choice(sizes)
    spot.shapesize(newsize)
  score = 0  
def start_game(): 
    global timer_up, score, timer
    score = 0 
    timer = 30
    timer_up = False
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    countdown()

spot.onclick(spot_clicked)
new_sizes()
new_color()
score_writer.penup()
score_writer.goto(-100, 100)
counter.penup()
counter.goto(-250, 100)
trtl.ontimer(countdown, counter_interval)
start_game()
trtl.mainloop()
