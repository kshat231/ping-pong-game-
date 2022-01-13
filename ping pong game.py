import turtle as t
import pygame
playerAscore=0
playerBscore=0

window=t.Screen()
window.title("ping pong game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(strech_width=5,length=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle=t.turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(strech_width=5,length=1)
rightpaddle.penup()
rightpaddle.goto(-350,0)

#creating ball

ball=t.turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating pen for scorecard update

pen=t.turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="centre",font=('arial',24,'normal'))



#moving the left paddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)


def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90 
    leftpaddle.sety(y)

#moving the right paddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)


def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90 
    rightpaddle.sety(y)   

#assign keys to play

window.listen()
window.onkeypress(leftpaddleup,"w")
window.onkeypress(leftpaddledown,"s")
window.onkeypress(rightpaddleup,"up")
window.onkeypress(rightpaddledown,"down")

while True:
    window.update()
    
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.setx(ball.ycor()+ballydirection)

    #settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("playerA:{}   playerb:{}".format(playerAscore,playerBscore),align='centre',font='arial')
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("playerA:{}   playerb:{}".format(playerAscore,playerBscore),align='centre',font='arial')


    #handling the collisions

    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
       ball.setx(340)
       ballxdirection=ballxdirection*-1

    
    if(ball.xcor()>-340)and(ball.xcor()<-350)and(ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
       ball.setx(-340)
       ballxdirection=ballxdirection*-1
       