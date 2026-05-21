import turtle
import time

WIDTH, HEIGHT = 800, 600
USER_HP, COM_HP = 100, 100
USER_SPEED = 25
COM_SPEED = 5
SHELL_SPEED = 14
USER_COOLDOWN, COM_COOLDOWN = 0.4, 0.8

last_user_shot_time = 0
last_com_shot_time = 0
user_shell_active = False
com_shell_active = False
game_state = "START"
game_start_time = 0

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("거북이 등껍질 대전")
screen.bgcolor("white")
screen.tracer(0)

divider = turtle.Turtle()
divider.hideturtle()
divider.speed(0)
divider.penup()
divider.goto(-WIDTH//2, 0)
divider.pendown()
divider.forward(WIDTH)

player_user = turtle.Turtle()
player_user.shape("turtle")
player_user.color("blue")
player_user.penup()
player_user.goto(0, -240)
player_user.setheading(90)

player_com = turtle.Turtle()
player_com.shape("turtle")
player_com.color("red")
player_com.penup()
player_com.goto(0, 240)
player_com.setheading(270)

shell_user = turtle.Turtle()
shell_user.shape("circle")
shell_user.color("cyan")
shell_user.penup()
shell_user.hideturtle()

shell_com = turtle.Turtle()
shell_com.shape("circle")
shell_com.color("orange")
shell_com.penup()
shell_com.hideturtle()

hud = turtle.Turtle()
hud.hideturtle()
hud.penup()

def draw_ui():
    hud.clear()
    hud.goto(-350, 250)
    hud.write(f"COM HP: {COM_HP}", font=("Arial", 16, "bold"))
    hud.goto(-350, -280)
    hud.write(f"USER HP: {USER_HP}", font=("Arial", 16, "bold"))

def show_start_screen():
    hud.clear()
    hud.goto(0, 0)
    hud.write("Press ENTER to Start", align="center", font=("Arial", 24, "bold"))

def reset_game():
    global USER_HP, COM_HP, user_shell_active, com_shell_active
    USER_HP, COM_HP = 100, 100
    user_shell_active = False
    com_shell_active = False
    player_user.goto(0, -240)
    player_com.goto(0, 240)
    shell_user.hideturtle()
    shell_com.hideturtle()

def press_enter():
    global game_state, game_start_time
    if game_state == "START":
        game_state = "PLAYING"
        game_start_time = time.time()
        draw_ui()
    elif game_state == "GAME_OVER":
        reset_game()
        game_state = "PLAYING"
        game_start_time = time.time()
        draw_ui()

def user_move_left():
    if game_state != "PLAYING": return
    x = player_user.xcor()
    if x > -370:
        player_user.setx(x - USER_SPEED)

def user_move_right():
    if game_state != "PLAYING": return
    x = player_user.xcor()
    if x < 370:
        player_user.setx(x + USER_SPEED)

def user_shoot():
    global last_user_shot_time, user_shell_active
    if game_state != "PLAYING": return
    current_time = time.time()
    if not user_shell_active and (current_time - last_user_shot_time >= USER_COOLDOWN):
        shell_user.goto(player_user.xcor(), player_user.ycor() + 20)
        shell_user.showturtle()
        user_shell_active = True
        last_user_shot_time = current_time

def com_ai():
    global last_com_shot_time, com_shell_active
    if game_state != "PLAYING": return
    user_x = player_user.xcor()
    com_x = player_com.xcor()
    
    if com_x < user_x - 5 and com_x < 370:
        player_com.setx(com_x + COM_SPEED)
    elif com_x > user_x + 5 and com_x > -370:
        player_com.setx(com_x - COM_SPEED)
        
    current_time = time.time()
    if not com_shell_active and abs(com_x - user_x) < 15:
        if current_time - last_com_shot_time >= COM_COOLDOWN:
            shell_com.goto(player_com.xcor(), player_com.ycor() - 20)
            shell_com.showturtle()
            com_shell_active = True
            last_com_shot_time = current_time

def move_shells():
    global user_shell_active, com_shell_active
    if game_state != "PLAYING": return
    
    if user_shell_active:
        shell_user.sety(shell_user.ycor() + SHELL_SPEED)
        if shell_user.ycor() > HEIGHT//2:
            shell_user.hideturtle()
            user_shell_active = False
            
    if com_shell_active:
        shell_com.sety(shell_com.ycor() - SHELL_SPEED)
        if shell_com.ycor() < -HEIGHT//2:
            shell_com.hideturtle()
            com_shell_active = False

def check_collisions():
    global COM_HP, USER_HP, user_shell_active, com_shell_active
    if game_state != "PLAYING": return
    
    if user_shell_active and shell_user.distance(player_com) < 25:
        COM_HP -= 10
        shell_user.hideturtle()
        user_shell_active = False
        draw_ui()
        
    if com_shell_active and shell_com.distance(player_user) < 25:
        USER_HP -= 10
        shell_com.hideturtle()
        com_shell_active = False
        draw_ui()

def check_game_over():
    global game_state
    if COM_HP <= 0 or USER_HP <= 0:
        game_state = "GAME_OVER"
        hud.goto(0, 0)
        if COM_HP <= 0 and USER_HP <= 0:
            hud.write("DRAW\nPress ENTER to Restart", align="center", font=("Arial", 24, "bold"))
        elif COM_HP <= 0:
            clear_time = time.time() - game_start_time
            hud.write(f"USER WIN! ({clear_time:.2f}s)\nPress ENTER to Restart", align="center", font=("Arial", 24, "bold"))
        else:
            hud.write("COM WIN...\nPress ENTER to Restart", align="center", font=("Arial", 24, "bold"))

def main():
    screen.listen()
    screen.onkeypress(user_move_left, "Left")
    screen.onkeypress(user_move_right, "Right")
    screen.onkeypress(user_shoot, "space")
    screen.onkeypress(press_enter, "Return")
    
    show_start_screen()
    
    while True:
        if game_state == "PLAYING":
            com_ai()
            move_shells()
            check_collisions()
            check_game_over()
            
        screen.update()
        time.sleep(0.01)
        
    screen.mainloop()

if __name__ == "__main__":
    main()