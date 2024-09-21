import random
import tkinter as tk

def roll():
    return random.randint(1, 6)

def start_game():
    global players, max_score, player_scores, player_idx
    try:
        players = int(entry_players.get())
        if not 2 <= players <= 4:
            raise ValueError("Oyuncu sayisi 2 ile 4 arasinda olmalidir.")
    except ValueError as e:
        lbl_result.config(text=str("Oyuncu Sayısını Giriniz."))
        return
    max_score = 10
    player_scores = [0] * players
    player_idx = 0
    next_turn()

def next_turn():
    global player_idx
    player_idx = (player_idx + 1) % players
    lbl_turn.config(text=f"{player_idx + 1}. OYUNCUNUN SIRASI",font=("Arial", 12, "bold"))
    btn_roll.config(state=tk.NORMAL)
    btn_skip.config(state=tk.NORMAL)

def roll_dice():
    global player_idx
    value = roll()
    if value == 1:
        player_scores[player_idx] = 0
        next_turn()
    else:
        player_scores[player_idx] += value
        lbl_score.config(text=f"Atilan sayi: {value}\nSkorunuz: {player_scores[player_idx]}",font=("Arial", 12, "bold"))
        if player_scores[player_idx] >= max_score:
            end_game()
    

def end_game():
    global max_score, player_scores
    winning_score = max(player_scores)
    winning_players = [i + 1 for i, score in enumerate(player_scores) if score == winning_score]
    lbl_result.config(text=f"{', '.join(map(str, winning_players))}. oyuncu: {winning_score} skoruyla kazandi!",font=("Arial", 12, "bold"))
    btn_roll.config(state=tk.DISABLED)
    btn_skip.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Zar Oyunu")
root.geometry("600x500")
root.config(bg="white")  


lbl_players = tk.Label(root, text="Oyuncu sayisini girin (2 - 4 arası):", fg="black", bg="white", font=("Arial", 12, "bold"))
lbl_players.pack(pady=(30, 0))  

entry_players = tk.Entry(root, fg="black", bg="white",font=("Arial", 12, "bold"))  # Giriş kutusu için renkler
entry_players.pack(pady=(0, 30))


btn_start = tk.Button(root, text="Oyunu Başlat", command=start_game, fg="black", bg="white", font=("Arial", 12, "bold"))
btn_start.pack(pady=15)

lbl_turn = tk.Label(root, text="", fg="black", bg="white")
lbl_turn.pack(pady=5)

btn_roll = tk.Button(root, text="Zar At", command=roll_dice, state=tk.DISABLED, fg="black", bg="white", font=("Arial", 12, "bold"))
btn_roll.pack(pady=10)

btn_skip = tk.Button(root, text="Turu Pas Geç", command=next_turn, state=tk.DISABLED, fg="black", bg="white", font=("Arial", 12, "bold"))
btn_skip.pack(pady=10)


lbl_score = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 12, "bold"))
lbl_score.pack(pady=5)

lbl_result = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 12, "bold"))
lbl_result.pack(pady=5)


root.mainloop()
