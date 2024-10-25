# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
totalScore = 0
font_setup = ("MonoLisa", 20, "Arial")
timer = 30
counter_interval = 1000  
timer_up = False
colors = ['pink', 'purple', 'green', 'red', 'blue', 'orange']
sizes = [0.5, 1, 1.5, 1.75, 2, 2.25]

#-----initialize turtle-----
wn = trtl.Screen()
wn.setup(width=500, height=500)
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
counter = trtl.Turtle()
trtl.bgcolor("mistyRose")

#-----game functions--------
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
    global totalScore
    score += 1
    score_writer.clear()
    score_writer.hideturtle()
    score_writer.write(totalScore, font=font_setup) 
def change_position():
    new_xpos = random.randint(-200, 200)
    new_ypos = random.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)
    update_score()
def spot_clicked(x, y):
    global timer_up
    if not timer_up:  #to check if ur still playing or not
        spot.penup()
        spot.hideturtle()
        change_position()
        spot.showturtle()
        spot.pendown()
        new_color()
        new_sizes()
def new_color(): #to give each spot a different color
    random_color = rand.choice(colors)
    spot.color(random_color)s
    spot.stamp()
    spot.color(spot_color)
def new_sizes(): #to make each spot a diff size randomly
    newsize = random.choice(sizes)
    spot.shapesize(newsize)
def start_game(): 
    global timer_up, score, timer
    score = 0
    timer = 30
    timer_up = False
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    countdown()

#-----events----------------
spot.onclick(spot_clicked)
new_sizes()
new_color()
score_writer.penup()
score_writer.goto(-100, 100)
counter.penup()
counter.goto(-250, 100)
wn.ontimer(countdown, counter_interval)
start_game()
wn.mainloop()
