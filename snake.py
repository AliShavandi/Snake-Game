import turtle
import time
import random

# Delayes the movement of objects so it is not super fast
delay = 0.1

# Score
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('light green')
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('yellow')
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align='center', font=('Courier', 28, "bold"))

# Border hit pen


# List of the snake body segments
segments = []

# Snake head directions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

# Snake head movement of each direction
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x= head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')


 

# Main gameloop
while True:
    # Updates the window
    wn.update()

    # Check for border collisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        
        # Game over pen
        bpen = turtle.Turtle()
        bpen.speed(0)
        bpen.shape('square')
        bpen.color('red')
        bpen.penup()
        bpen.ht()
        bpen.goto(0, 0)
        bpen.write("OUCH! BORDER HIT", align='center', font=('Courier', 40, 'bold'))
        
        # Snake reset
        head.goto(0,0)
        head.direction = 'stop'
        time.sleep(2.5)
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the dealy 
        delay = 0.1
      
        # Delete the game over pen
        bpen.clear()
        # Update the score
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align='center', font=('Courier', 28, "bold"))


    # Snake head and food collision
    if head.distance(food) < 20:
        # Moves the food into a random spot on the window
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)
        # Add snake body segments
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.0001

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align='center', font=('Courier', 28, "bold"))
        

    
    # Attach the segments to the snake head
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Calls the move function to make the snake move
    move()

    # Check for head collisions with the body
    for segment in segments:
        if segment.distance(head) < 20:
        # Game over pen
            bodypen = turtle.Turtle()
            bodypen.speed(0)
            bodypen.shape('square')
            bodypen.color('red')
            bodypen.penup()
            bodypen.ht()
            bodypen.goto(0, 0)
            bodypen.write("OWIE! BODY COLLISION", align='center', font=('Courier', 40, 'bold'))
            time.sleep(2.5)
            head.goto(0,0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()           
            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            bodypen.clear()

            pen.clear()
            pen.write("Score: {}   High Score: {}".format(score, high_score), align='center', font=('Courier', 28, "bold"))



    # Delays the animation speed of the turtles
    time.sleep(delay)

wn.mainloop()
