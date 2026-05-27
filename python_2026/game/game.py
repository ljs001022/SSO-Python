import turtle as t
import random
import time

# ==========================================
# 1. 게임 기본 설정 및 초기 데이터
# ==========================================
screen = t.Screen()
screen.setup(1000, 850)
screen.title("데이터 기반 거북이 분산 투자 시뮬레이션")
screen.bgcolor("#1e1e1e")
screen.tracer(0)

assets = {
    "User": 100,
    "Com1": 100,
    "Com2": 100,
    "Com3": 100,
    "Com4": 100
}

colors = ["red", "orange", "yellow", "green", "blue"]
turtles = []

scoreboard = t.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color("white")

log_board = t.Turtle()
log_board.hideturtle()
log_board.penup()
log_board.color("#a0a0a0")
log_lines = []

def create_turtles():
    for i in range(5):
        if len(turtles) < 5:
            turtle = t.Turtle()
            turtle.shape("turtle")
            turtle.color(colors[i])
            turtle.penup()
            turtles.append(turtle)
        turtles[i].goto(-450, 100 - (i * 65))
    screen.update()

def draw_stadium():
    line = t.Turtle()
    line.hideturtle()
    line.speed(0)
    line.color("white")
    line.penup()
    
    line.goto(-500, 150)
    line.pendown()
    line.goto(500, 150)
    
    line.penup()
    line.goto(-500, -220)
    line.pendown()
    line.goto(500, -220)
    
    line.penup()
    line.goto(400, 130)
    line.pendown()
    line.goto(400, -200)
    screen.update()

def update_gui_scoreboard(total_bets, user_bets):
    scoreboard.clear()
    
    scoreboard.goto(-450, 380)
    scoreboard.write("[ 플레이어 코인 현황 ]", font=("Arial", 12, "bold"))
    
    asset_text = f"User: {assets['User']} | Com1: {assets['Com1']} | Com2: {assets['Com2']} | Com3: {assets['Com3']} | Com4: {assets['Com4']}"
    scoreboard.goto(-450, 350)
    scoreboard.write(asset_text, font=("Arial", 14, "normal"))
    
    scoreboard.goto(-450, 300)
    scoreboard.write("[ 거북이별 실시간 투자 및 배당률 ]", font=("Arial", 12, "bold"))
    
    total_pool = sum(total_bets)
    line1_text = ""
    line2_text = ""
    
    for i in range(5):
        if total_bets[i] > 0:
            est_dividend = f"{total_pool / total_bets[i]:.1f}배"
        else:
            est_dividend = "0.0배"
            
        info = f"[{colors[i].upper()}] 총:{total_bets[i]} (내투자:{user_bets[i]} / 예상:{est_dividend})    "
        
        if i < 3:
            line1_text += info
        else:
            line2_text += info
            
    scoreboard.goto(-450, 265)
    scoreboard.write(line1_text, font=("Arial", 11, "normal"))
    
    scoreboard.goto(-450, 235)
    scoreboard.write(line2_text, font=("Arial", 11, "normal"))
    screen.update()

def log_to_gui(text):
    print(text)
    log_lines.append(text)
    if len(log_lines) > 6:
        log_lines.pop(0)
        
    log_board.clear()
    start_y = -250
    for line in log_lines:
        log_board.goto(-450, start_y)
        log_board.write(line, font=("Arial", 11, "normal"))
        start_y -= 22
    screen.update()

draw_stadium()
create_turtles()
log_to_gui("[SYSTEM] 게임이 준비되었습니다. 베팅을 진행하세요.")

# ==========================================
# 2. 베팅 및 배당률 계산 로직
# ==========================================
def run_betting_phase():
    total_bets_on_turtle = [0, 0, 0, 0, 0]
    all_player_bets = {
        "User": [0, 0, 0, 0, 0], "Com1": [0, 0, 0, 0, 0],
        "Com2": [0, 0, 0, 0, 0], "Com3": [0, 0, 0, 0, 0], "Com4": [0, 0, 0, 0, 0]
    }
    
    for com in ["Com1", "Com2", "Com3", "Com4"]:
        available = assets[com]
        for i in range(5):
            if available >= 10:
                bet = random.choice([0, 10, 20])
                if available >= bet:
                    total_bets_on_turtle[i] += bet
                    all_player_bets[com][i] = bet
                    available -= bet
        assets[com] = available

    update_gui_scoreboard(total_bets_on_turtle, all_player_bets["User"])
    log_to_gui("[INVESTMENT] 컴퓨터들의 투자가 완료되었습니다. 배당률을 확인하세요.")

    while assets["User"] >= 10:
        u_input = screen.textinput("분산 투자 단계", 
            f"코인을 걸 거북이 번호(1~5)를 입력하세요.\n(경기를 시작하려면 '0' 입력 / 남은 코인: {assets['User']})")
        
        if u_input == '0' or u_input is None:
            break
            
        if u_input in ['1', '2', '3', '4', '5']:
            idx = int(u_input) - 1
            total_bets_on_turtle[idx] += 10
            all_player_bets["User"][idx] += 10
            assets["User"] -= 10
            
            update_gui_scoreboard(total_bets_on_turtle, all_player_bets["User"])
            log_to_gui(f"-> User가 {idx+1}번 거북이에게 10코인을 투자했습니다.")
        else:
            pass

    return total_bets_on_turtle, all_player_bets

# ==========================================
# 3. 레이싱 시뮬레이션 및 순위 매기기
# ==========================================
def start_race():
    log_to_gui("🏁 경주를 시작합니다! 거북이들의 속도는 2초마다 변합니다.")
    
    speeds = [random.randint(2, 8) for _ in range(5)]
    last_speed_update = time.time()
    finished_order = []
    
    while len(finished_order) < 5:
        screen.update()
        time.sleep(0.01)
        
        if time.time() - last_speed_update > 2:
            speeds = [random.randint(2, 8) for _ in range(5)]
            last_speed_update = time.time()
            
        for i in range(5):
            if i not in finished_order:
                turtles[i].forward(speeds[i])
                if turtles[i].xcor() >= 400:
                    finished_order.append(i)
                    log_to_gui(f"🏆 {len(finished_order)}등: {i+1}번 거북이 ({colors[i].upper()})")

    return finished_order

# ==========================================
# 4. 정산 로직
# ==========================================
def distribute_rewards(total_bets, all_player_bets, winner_idx):
    total_pool = sum(total_bets)
    winner_pool = total_bets[winner_idx]
    
    log_to_gui(f"[결과] 우승: {winner_idx+1}번 거북이 ({colors[winner_idx].upper()})")
    
    if winner_pool == 0:
        log_to_gui("[정산] 승리한 거북이에 투자한 플레이어가 없어 판돈이 소멸됩니다.")
        return

    dividend_rate = total_pool / winner_pool
    log_to_gui(f"[배당] 최종 배당률: {dividend_rate:.2f}배")
    
    for name in assets.keys():
        bet_amount = all_player_bets[name][winner_idx]
        reward = int(bet_amount * dividend_rate)
        assets[name] += reward
        if reward > 0:
            log_to_gui(f" -> {name} 배당금 획득: +{reward} 코인")
            
    update_gui_scoreboard(total_bets, all_player_bets["User"])

# ==========================================
# 5. 메인 게임 프로세스 루프
# ==========================================
def game_loop():
    while True:
        create_turtles()
        
        total_bets, all_player_bets = run_betting_phase()
        
        finished_order = start_race()
        winner_idx = finished_order[0]
        
        distribute_rewards(total_bets, all_player_bets, winner_idx)
        
        answer = screen.textinput("게임 종료", "한 판 더 하시겠습니까? (y/n)").lower()
        if answer != 'y':
            log_to_gui("게임을 종료합니다. 최종 자산 상태를 확인하세요.")
            break

game_loop()
t.mainloop()