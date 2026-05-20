import turtle as t

t.shape('turtle')

def pUp(): t.penup()
def pDown(): t.pendown()

def init():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()

t.onkeypress(pUp, 'u')
t.onkeypress(pDown, 'd')
t.onkeypress(init, 'Escape')

t.onscreenclick(t.goto)

t.listen()
t.mainloop()