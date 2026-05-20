import random
import time

# ==========================================
# 1. 상수 및 패 데이터 정의
# ==========================================
INIT_MONEY = 1000
BET_BASE = 50

CARD_POOL = [
    (1, "광"), (1, "피"), (2, "열"), (2, "띠"), (3, "광"), (3, "피"),
    (4, "열"), (4, "띠"), (5, "열"), (5, "띠"), (6, "열"), (6, "띠"),
    (7, "열"), (7, "띠"), (8, "광"), (8, "열"), (9, "열"), (9, "띠"),
    (10, "장"), (10, "풍")
]

CARD_NAMES = {
    (1, "광"): "1광", (1, "피"): "1피", (2, "열"): "2열", (2, "띠"): "2띠",
    (3, "광"): "3광", (3, "피"): "3피", (4, "열"): "4열", (4, "띠"): "4띠",
    (5, "열"): "5열", (5, "띠"): "5띠", (6, "열"): "6열", (6, "띠"): "6띠",
    (7, "열"): "7열", (7, "띠"): "7띠", (8, "광"): "8광", (8, "열"): "8열",
    (9, "열"): "9열", (9, "띠"): "9띠", (10, "장"): "10장", (10, "풍"): "10풍"
}

# ==========================================
# 2. 족보 및 가중치 계산 엔진
# ==========================================
def evaluate_hand(card1, card2=None):
    if card2 is None:
        w, t = card1
        if t == "광": return (50 + w, f"{w}광 예비", None)
        if w == 10: return (40, "10월 예비", None)
        return (w * 3, f"{w}월 예비", None)

    c1, c2 = sorted([card1, card2], key=lambda x: x[0])
    w1, t1 = c1
    w2, t2 = c2

    if t1 == "광" and t2 == "광":
        if w1 == 3 and w2 == 8: return (100, "3·8광땡", None)
        if w1 == 1 and w2 == 3: return (99, "1·3광땡", None)
        if w1 == 1 and w2 == 8: return (98, "1·8광땡", None)

    is_amhaeng = (w1 == 4 and w2 == 7 and ((t1 == "열" and t2 == "띠") or (t1 == "띠" and t2 == "열")))
    is_ttangjabi = (w1 == 3 and w2 == 7)
    is_mung_gusa = (w1 == 4 and w2 == 9 and t1 == "열" and t2 == "열")
    is_gusa = (w1 == 4 and w2 == 9 and not is_mung_gusa)

    if w1 == w2:
        if w1 == 10: return (90, "장땡", None)
        return (80 + w1, f"{w1}땡", None)

    if w1 == 1 and w2 == 2: return (70, "알리 (1·2)", None)
    if w1 == 1 and w2 == 4: return (69, "독사 (1·4)", None)
    if w1 == 1 and w2 == 9: return (68, "구삥 (1·9)", None)
    if w1 == 1 and w2 == 10: return (67, "장삥 (1·10)", None)
    if w1 == 4 and w2 == 10: return (66, "장사 (10·4)", None)
    if w1 == 4 and w2 == 6: return (65, "세륙 (4·6)", None)

    if is_amhaeng: return (1, "7·4 암행어사", "amhaeng")    
    if is_ttangjabi: return (0, "7·3 땡잡이", "ttangjabi")  
    if is_mung_gusa: return (3, "멍텅구리구사", "mung_gusa") 
    if is_gusa: return (3, "4·9 파토", "gusa")              

    score = (w1 + w2) % 10
    score_names = {
        9: "갑오 (아홉끗)", 8: "여덟끗", 7: "일곱끗", 6: "여섯끗",
        5: "다섯끗", 4: "네끗", 3: "세끗", 2: "두끗", 1: "한끗", 0: "망통 (0끗)"
    }
    return (score, score_names[score], None)


# ==========================================
# 3. 컴퓨터(COM) 베팅 인공지능 (AI)
# ==========================================
class ComAI:
    @staticmethod
    def get_action(com_money, call_amount, total_pot, round_num, com_cards):
        if len(com_cards) == 1:
            score, _, _ = evaluate_hand(com_cards[0])
            card_strength = score / 60.0
        else:
            score, _, flag = evaluate_hand(com_cards[0], com_cards[1])
            if flag in ["amhaeng", "ttangjabi", "mung_gusa", "gusa"]:
                card_strength = 0.45
            else:
                card_strength = score / 100.0

        if random.random() < 0.10:
            card_strength += 0.25

        if com_money <= call_amount:
            if card_strength > 0.35 or call_amount <= BET_BASE * 2:
                return '콜', call_amount
            return '다이', 0

        if call_amount == 0:
            if card_strength >= 0.80:
                bet = int(total_pot * 0.5)
                return '하프', bet
            elif card_strength >= 0.55:
                bet = int(total_pot * 0.25)
                return '쿼터', bet
            elif card_strength >= 0.30:
                return '삥', BET_BASE
            else:
                return '체크', 0
        else:
            if call_amount > total_pot * 0.8 and card_strength < 0.4:
                return '다이', 0

            if card_strength >= 0.85:
                bet_pure = int((total_pot + call_amount) * 0.5)
                return '하프', call_amount + bet_pure
            elif card_strength >= 0.60:
                bet_pure = int((total_pot + call_amount) * 0.25)
                return '쿼터', call_amount + bet_pure
            elif card_strength >= 0.25:
                return '콜', call_amount
            else:
                return '다이', 0


# ==========================================
# 4. 베팅 시스템 매니저
# ==========================================
class SeotdaGame:
    def __init__(self):
        self.user_money = INIT_MONEY
        self.com_money = INIT_MONEY
        self.accumulated_pot = 0
        self.sun = "user"

    def print_status(self, current_pot):
        print("\n" + "="*45)
        print(f"💰 [현재 재화 현황]  나: {self.user_money}냥 | 컴퓨터: {self.com_money}냥")
        print(f"🍯 [현재 판돈] 총 {current_pot}냥 (이월금: {self.accumulated_pot}냥)")
        print("="*45)

    def execute_betting_round(self, round_num, user_cards, com_cards, current_pot):
        user_round_bet = 0
        com_round_bet = 0
        
        user_acted = False
        com_acted = False
        turn = self.sun

        while True:
            if user_acted and com_acted and (user_round_bet == com_round_bet):
                break
                
            if (self.user_money == 0 or self.com_money == 0) and (user_round_bet == com_round_bet):
                break

            # --------------------------------------
            # USER TURN
            # --------------------------------------
            if turn == "user":
                call_amount = com_round_bet - user_round_bet
                
                print(f"\n🟢 [나의 턴] 내 패: " + ", ".join([CARD_NAMES[c] for c in user_cards]))
                if round_num == 1:
                    _, name, _ = evaluate_hand(user_cards[0])
                    print(f"🔮 [1장 예상 족보]: {name}")
                else:
                    _, name, _ = evaluate_hand(user_cards[0], user_cards[1])
                    print(f"🎴 [최종 확인 족보]: {name}")

                options = ["다이"]
                if call_amount == 0:
                    options.append("체크")
                    options.append("삥")
                else:
                    options.append("콜")
                options.append("쿼터")
                options.append("하프")

                print(f"👉 선택 가능: {', '.join(options)} (콜 비용: {call_amount}냥)")
                
                action = ""
                while action not in options:
                    action = input("행동을 입력하세요: ").strip()

                bet_amount = 0
                if action == "다이":
                    return "user_die", current_pot
                elif action == "체크":
                    bet_amount = 0
                elif action == "삥":
                    bet_amount = BET_BASE
                elif action == "콜":
                    bet_amount = call_amount
                elif action == "쿼터":
                    quarter_pure = int((current_pot + call_amount) * 0.25)
                    bet_amount = call_amount + quarter_pure
                elif action == "하프":
                    half_pure = int((current_pot + call_amount) * 0.5)
                    bet_amount = call_amount + half_pure

                max_allowed = self.com_money + call_amount
                if bet_amount > max_allowed:
                    bet_amount = max_allowed

                is_all_in = False
                if bet_amount >= self.user_money:
                    bet_amount = self.user_money
                    is_all_in = True

                self.user_money -= bet_amount
                user_round_bet += bet_amount
                current_pot += bet_amount
                
                display_action = f"{action}(올인)" if is_all_in else action
                print(f"▶ [USER] {display_action} 베팅! (-{bet_amount}냥)")
                
                user_acted = True
                
                if self.user_money == 0 and user_round_bet <= com_round_bet:
                    self.print_status(current_pot)
                    break

                turn = "com"

            # --------------------------------------
            # COMPUTER TURN
            # --------------------------------------
            else:
                call_amount = user_round_bet - com_round_bet
                
                print(f"\n🔴 [컴퓨터 턴] 생각 중...")
                time.sleep(1)
                
                action, bet_amount = ComAI.get_action(
                    self.com_money, call_amount, current_pot, round_num, com_cards
                )

                if action == "다이":
                    print("▶ [COM] 다이! 기권했습니다.")
                    return "com_die", current_pot
                
                max_allowed = self.user_money + call_amount
                if bet_amount > max_allowed:
                    bet_amount = max_allowed

                is_all_in = False
                if bet_amount >= self.com_money:
                    bet_amount = self.com_money
                    is_all_in = True

                self.com_money -= bet_amount
                com_round_bet += bet_amount
                current_pot += bet_amount
                
                display_action = f"{action}(올인)" if is_all_in else action
                print(f"▶ [COM] {display_action} 베팅! (-{bet_amount}냥)")

                com_acted = True
                
                if self.com_money == 0 and com_round_bet <= user_round_bet:
                    self.print_status(current_pot)
                    break

                turn = "user"

            self.print_status(current_pot)

        return "continue", current_pot

    def play_round(self):
        print(f"\n🎲 섰다 게임을 시작합니다! (현재 선: {self.sun.upper()})")
        
        if self.user_money < BET_BASE or self.com_money < BET_BASE:
            print("❌ 기본 베팅 금액이 부족하여 게임을 진행할 수 없습니다.")
            return False
            
        self.user_money -= BET_BASE
        self.com_money -= BET_BASE
        current_pot = (BET_BASE * 2) + self.accumulated_pot
        self.accumulated_pot = 0
        
        self.print_status(current_pot)

        deck = CARD_POOL.copy()
        random.shuffle(deck)

        user_cards = [deck.pop()]
        com_cards = [deck.pop()]

        print("\n--- 🎴 [1 라운드] 첫 번째 패 분배 ---")
        result, current_pot = self.execute_betting_round(1, user_cards, com_cards, current_pot)

        if result == "user_die":
            print("\n🏳️ 당신이 기권했습니다. 컴퓨터 승리!")
            self.com_money += current_pot
            self.sun = "com"
            return True
        elif result == "com_die":
            print("\n🎉 컴퓨터가 기권했습니다. 당신의 승리!")
            self.user_money += current_pot
            self.sun = "user"
            return True

        user_cards.append(deck.pop())
        com_cards.append(deck.pop())

        print("\n--- 🎴 [2 라운드] 두 번째 패 분배 ---")
        result, current_pot = self.execute_betting_round(2, user_cards, com_cards, current_pot)

        if result == "user_die":
            print("\n🏳️ 당신이 기권했습니다. 컴퓨터 승리!")
            self.com_money += current_pot
            self.sun = "com"
            return True
        elif result == "com_die":
            print("\n🎉 컴퓨터가 기권했습니다. 당신의 승리!")
            self.user_money += current_pot
            self.sun = "user"
            return True

        print("\n" + "="*20 + " 오픈 및 결과 확인 " + "="*20)
        user_score, user_hand_name, user_flag = evaluate_hand(user_cards[0], user_cards[1])
        com_score, com_hand_name, com_flag = evaluate_hand(com_cards[0], com_cards[1])

        print(f"▶ 나의 패   : [{CARD_NAMES[user_cards[0]]}], [{CARD_NAMES[user_cards[1]]}] ➡️ {user_hand_name}")
        print(f"▶ 컴퓨터 패 : [{CARD_NAMES[com_cards[0]]}], [{CARD_NAMES[com_cards[1]]}] ➡️ {com_hand_name}")
        print("-" * 50)

        is_pato = False
        pato_reason = ""

        if user_flag == "gusa" and com_score <= 70:
            is_pato = True
            pato_reason = f"나의 {user_hand_name}"
        elif com_flag == "gusa" and user_score <= 70:
            is_pato = True
            pato_reason = f"컴퓨터의 {com_hand_name}"

        if user_flag == "mung_gusa" and com_score <= 90:
            is_pato = True
            pato_reason = f"나의 {user_hand_name}"
        elif com_flag == "mung_gusa" and user_score <= 90:
            is_pato = True
            pato_reason = f"컴퓨터의 {com_hand_name}"

        if is_pato:
            print(f"📢 특수 족보 [{pato_reason}] 권한 발동! 이번 판은 무효 및 재경기 처리됩니다.")
            print(f"💰 판돈 {current_pot}냥은 다음 판으로 이월됩니다.")
            self.accumulated_pot = current_pot
            return True

        if user_flag == "amhaeng" and com_score in [98, 99]:
            print(f"⚔️ 나의 [7·4 암행어사]가 컴퓨터의 암행어사 표적 [{com_hand_name}]를 격파했습니다!")
            user_score = 101  
        elif com_flag == "amhaeng" and user_score in [98, 99]:
            print(f"⚔️ 컴퓨터의 [7·4 암행어사]가 나의 암행어사 표적 [{user_hand_name}]를 격파했습니다!")
            com_score = 101

        if user_flag == "ttangjabi" and (81 <= com_score <= 89):
            print(f"⚔️ 나의 [7·3 땡잡이]가 컴퓨터의 [{com_hand_name}]를 사냥했습니다!")
            user_score = 95   
        elif com_flag == "ttangjabi" and (81 <= user_score <= 89):
            print(f"⚔️ 컴퓨터의 [7·3 땡잡이]가 나의 [{user_hand_name}]를 사냥했습니다!")
            com_score = 95

        if user_score > com_score:
            print(f"🏆 승리! 당신이 {current_pot}냥을 획득했습니다.")
            self.user_money += current_pot
            self.sun = "user"
        elif user_score < com_score:
            print(f"🤖 컴퓨터 승리! 컴퓨터가 {current_pot}냥을 가져갑니다.")
            self.com_money += current_pot
            self.sun = "com"
        else:
            print("🤝 무승부(비김)! 판돈이 다음 판으로 전액 이월됩니다.")
            self.accumulated_pot = current_pot

        return True


# ==========================================
# 5. 게임 메인 루프 실행
# ==========================================
if __name__ == "__main__":
    game = SeotdaGame()
    round_cnt = 1
    
    while True:
        print(f"\n\n{'✨' * 15} 제 {round_cnt} 라운드 {'✨' * 15}")
        success = game.play_round()
        
        if not success or game.user_money <= 0 or game.com_money <= 0:
            print("\n☠️ 한 플레이어의 재화가 모두 소진되었거나 게임을 지속할 수 없어 종료합니다.")
            print(f"최종 스코어 - 나: {game.user_money}냥 | 컴퓨터: {game.com_money}냥")
            break
            
        retry = input("\n🔄 새 판을 시작하려면 [Enter]를 눌러주세요 (종료하려면 아무 키나 입력 후 Enter): ").strip()
        if retry != '':
            print("게임을 종료합니다.")
            break
        round_cnt += 1

    # [추가] 메인 루프 탈출 후 cmd 창이 자동으로 바로 꺼지지 않도록 붙잡아두는 대기 코드
    print("\n" + "="*45)
    input("🚪 프로그램이 종료되었습니다. 창을 닫으려면 [Enter] 키를 누르세요...")