import turtle

# Initialize game variables
score = 0
lives = 2
colors = ["red", "green", "blue", "orange", "yellow", "white" ] # List of colors for the ball

#window screen setup
window = turtle.Screen()
window.title("DX Ball Game - Diagon Alley")
window.bgcolor("Black")
window.setup(width=800, height=600)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=10)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.width(5)
ball.penup()
ball.color(colors[0]) # Set initial ball color to the first color in the list
ball.pensize(5)
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3
ball.speed(5)

# Create the score 
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.goto(-380, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))

#Create lives displays
lives_display = turtle.Turtle()
lives_display.color("white")
lives_display.penup()
lives_display.goto(260, 260)
lives_display.write(f"Lives: {lives}", font=("Arial", 16, "bold"))

# Game over display
gameover_display = turtle.Turtle()
gameover_display.hideturtle()
gameover_display.color("red")
gameover_display.penup()
gameover_display.goto(0, 0)


# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for border collisions
    if ball.xcor() > 380 or ball.xcor() < -380:
       ball.dx *= -1
       ball.color(colors[score % len(colors)])  # Change ball color
    elif ball.ycor() > 280:
       ball.dy *= -1
    elif ball.xcor() == 380 or ball.xcor() == -380:
       ball.color(colors[score % len(colors)])  # Change ball color


    # Check for paddle collision
    if ball.ycor() < -240 and ball.ycor() > -250 and (ball.xcor() > paddle.xcor() - 60 and ball.xcor() < paddle.xcor() + 60):
        ball.dy *= -1
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

    # Check for missed ball
    if ball.ycor() < -280:
        lives -= 1
        lives_display.clear()
        lives_display.write(f"Lives: {lives}", font=("Arial", 16, "normal"))
        if lives == 0:
            gameover_display.showturtle(gameover_display.write("Game Over", align="center", font=("Arial", 40, "bold")))
            ball.hideturtle()
            window.update()
            turtle.done()
        else:
            ball.goto(0, 0)
            ball.dx *= -1
            ball.dy *= -1
            
       # Move the paddle
    def move_left():
        x = paddle.xcor()
        x -= 20
        if x < -380:
            x = -380
        paddle.setx(x)

    def move_right():
        x = paddle.xcor()
        x += 20
        if x > 380:
            x = 380
        paddle.setx(x)

    window.listen()
    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")

