import turtle as t
import random

#화면
screen = t.Screen()
screen.title('feeding turtle')  # 수정 필요
screen.colormode(255)
screen.bgcolor(2,28,17) # 수정 필요
screen.setup(700,700)
# screen.addshape('turtle')
# screen.addshape('turtle')
# screen.addshape('turtle')

#player
p = t.Turtle()
p.shape('turtle')
p.setheading(90)
p.penup()
p.goto(0,200)
p.color(194,172,54)
p.pencolor('white')
p.pensize(2)
p.shapesize(1.5,1.5)
p.speed(0)

#적
e = t.Turtle()
e.setheading(90)
e.shape('turtle')
e.color('salmon')
e.shapesize(1.5,1.5)
e.pencolor('black')
e.penup()
e.speed(0)
e.goto(0,-100)

#먹이
f1 = t.Turtle()
f1.shape('turtle')
f1.shapesize(1,1)
f1.penup()
f1.speed(0)
f1.goto(-100,0)

f2 = t.Turtle()
f2.shape('turtle')
f2.shapesize(0.8,0.8)
f2.penup()
f2.speed(0)
f2.goto(0,0)

f3 = t.Turtle()
f3.shape('turtle')
f3.shapesize(0.5,0.5)
f3.penup()
f3.speed(0)
f3.goto(100,0)

#점수
score = 0

s = t.Turtle()
s.hideturtle()
s.color(12,184,112)
s.penup()
s.goto(0,250)
s.write('Score: 0',align='center',font=('Arial',20,'bold'))

prs = t.Turtle()
prs.hideturtle()
prs.color(194,17,99)
prs.penup()
prs.goto(0,-500)

st = t.Turtle()
st.hideturtle()
st.penup()
st.goto(250, 200)
st.color('orange')
st.write('당근 x 1',align='right',font=('맑은 고딕',15,'bold'))

st.goto(250, 160)
st.color('lightgreen')
st.write('오이 x 3',align='right',font=('맑은 고딕',15,'bold'))

st.goto(250, 120)
st.color('green')
st.write('상추 x 5',align='right',font=('맑은 고딕',15,'bold'))

#먹이 위치
def foodlocation1():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    f1.goto(x,y)

def foodlocation2():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    f2.goto(x,y)

def foodlocation3():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    f3.goto(x,y)

#점수 표시
def score1():
    s.clear()
    s.goto(0,300)
    s.write('Score:'+str(score),align='center',font=('Arial',20,'bold'))

def score2():
    s.clear()
    s.goto(0,300)
    s.write('Score:'+str(score),align='center',font=('Arial',20,'bold'))

def score3():
    s.clear()
    s.goto(0,300)
    s.write('Score:'+str(score),align='center',font=('Arial',20,'bold'))

#먹이 먹음
def check():
    global score

    if p.distance(f1) < 40:
        score += 1
        score1()
        foodlocation1()
    elif p.distance(f2) < 40:
        score += 3
        score2()
        foodlocation2()
    elif p.distance(f3) < 40:
        score += 5
        score3()
        foodlocation3()

#적 이동
def e1():
    e.setheading(e.towards(p))
    e.forward(15)
    if e.distance(p) < 30:
        gameover()
    else:
        screen.ontimer(e1,80)

# 게임 오버
go = t.Turtle()
go.hideturtle()
go.color('tomato')
go.penup()
go.goto(0, -200)

def gameover():
    go.clear()
    go.goto(0, -200)
    go.write('GAME OVER', align='center', font=('Arial',20,'bold'))

#방향키
def r():
    p.setheading(0)
    p.forward(15)
    check()

def u():
    p.setheading(90)
    p.forward(15)
    check()

def l():
    p.setheading(180)
    p.forward(15)
    check()

def d():
    p.setheading(270)
    p.forward(15)
    check()

t.onkeypress(r, 'Right')
t.onkeypress(u, 'Up')
t.onkeypress(l, 'Left')
t.onkeypress(d, 'Down')

#시작
def start():
    global score

    score = 0
    score1()

    prs.clear()
    go.clear()

    p.goto(0, 200)
    e.goto(0, -100)
    foodlocation1()
    foodlocation2()
    e1()

    prs.clear()

prs.goto(0,-200)
prs.write('Press SPACE to Start',align='center',font=('Arial', 30, 'bold'))
screen.onkeypress(start,'space')

#
t.listen()
t.mainloop()