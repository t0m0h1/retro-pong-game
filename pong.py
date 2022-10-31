#Welcome to my pong game (retro/simple)
# This uses the turtle drawing module
from glob import escape
import turtle
import sys


#make sure to use full screen or set the screen size smaller if using mini screen
# or just add a border 

wn = turtle.Screen()
wn.title=("Pong by @TomHH")
wn.bgcolor("gray2")
wn.setup(width=800, height=600)
wn.tracer(0)


#score
#you increase score whem ball goes off the screen

score_a = 0        
score_b = 0

#border draw code


#first paddle (a)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#2nd paddle (b)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#ball (draw code)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)

#ball movement

ball.dx = 2
ball.dy = -2


#pen stuff (turtle)

pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()#text only
pen.goto(0, 260)
pen.write("RETRO PONG by @Tom H", align="center", font=("PT Mono", 28, "normal"))
pen.goto(0, 140)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))
pen.goto(0, 10)
pen.color("white")
pen.write("left paddle (W & S) right paddle (P & L)", align="center", font=("courier", 24, "normal"))
pen.color("orange")

#white orange text, white, back to orange

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#bind keyboard

#We are using W and S keys to control the left paddle, and up and down keys to control the right paddle!


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "p")
wn.onkeypress(paddle_b_down, "l")
wn.onkeypress(sys.exit, 'e')


def close():
     wn.onkeypress(wn.bye, "Escape")
     close = turtle.Turtle()
     close.hideturtle()

wn.onkeypress(close, "Escape")
wn.listen()


#main game loop

while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border stuff
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


    #score count increases by one (score = score + 1)

    #player win loop (best of 10)

    if score_a >= 2:
        pen.goto(0, 100)
        pen.color("red")
        pen.write("Player A wins!".format(score_a, score_b), align="center", font=("courier", 30, "normal"))
        pen.goto(0, -150)
        pen.write("double tap 'esc' to exit", align="center", font=("courier", 30, "normal"))
        ball.goto(0, 0)
        ball.hideturtle()

        
    if score_b >= 2:
        pen.goto(0, 100)
        pen.color("red")
        pen.write("Player B wins!".format(score_a, score_b), align="center", font=("courier", 30, "normal"))
        pen.goto(0, -150)
        pen.write("double tap 'esc' to exit!", align="center", font=("courier", 30, "normal"))
        ball.goto(0, 0)
        ball.hideturtle()
       


#paddle collide events
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1






# other close game code





    # def exit_game():
    #     sys.exit()
    
    # def close():
    #     wn.listen()
    #     wn.onkeypress(exit_game, "Escape")
    
    # wn.listen()
    # wn.onkeypress(close, "Escape")
    # wn.mainloop()