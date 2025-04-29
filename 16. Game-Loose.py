import random

def is_game_over(stones):
    return stones == 0

def get_possible_moves(stones):
    upper_bound = min(stones, 3)
    return list(range(1, upper_bound + 1))

def minimax(stones):
    if is_game_over(stones):
        return -1
    
    possible_moves = get_possible_moves(stones)
    for stones_to_remove in possible_moves:
        next_stones = stones - stones_to_remove # applying move
        if minimax(next_stones) == -1:
            return 1
    return -1


def find_best_move(stones):
    possible_moves = get_possible_moves(stones)

    for stones_to_remove in possible_moves:
        next_stones = stones - stones_to_remove # applying move
        if minimax(next_stones) == 1: # 1: next player wins, we lose
            return stones_to_remove

    return random.choice(possible_moves) # no winning move found

def get_human_move(stones):
    max_allowed = min(stones, 3)
    prompt = f"stones to remove (1 to {max_allowed}): "

    while True:
        try:
            stones_str = input(prompt)
            stones_to_remove = int(stones_str)
            if not (1 <= stones_to_remove <= max_allowed):
                print(f"Invalid number of stones. Must be between 1 and {max_allowed}.")
                continue
            return stones_to_remove
        
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_nim_single():
    stones = 21
    current_player = random.choice(["Human", "AI"])
    print(f"starting player: {current_player}")

    while not is_game_over(stones):
        print(f"\nstones: {stones}")
        print(f"{current_player}'s turn.")

        if current_player == "Human":
            move = get_human_move(stones)
        else: 
            move = find_best_move(stones)
            print(f"AI removes {move} stone(s).")

        stones = stones - move # apply move
        current_player = "AI" if current_player == "Human" else "Human" # switch players

    print(f"\nstones: {stones}")
    print("game over!")
    winner = "AI" if current_player == "Human" else "Human" # the player who cannot make a move loses
    print(f"{winner} wins!")

play_nim_single()