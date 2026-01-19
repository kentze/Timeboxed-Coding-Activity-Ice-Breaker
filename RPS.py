import random

# ==========================================
# 🟢 MEMBER A: Input Manager
# ==========================================
def get_player_choice():
    """
    Prompts the user to enter their move.
    Checks if the input is valid (rock, paper, or scissors).
    Returns: A string ('rock', 'paper', or 'scissors').
    """
    # TODO: Member A writes code here
    # 1. Use input() to get user choice
    # 2. Use a loop (while) to ensure valid input
    return "rock" # Placeholder return value


# ==========================================
# 🔵 MEMBER B: Game Logic (Referee)
# ==========================================
def get_computer_choice():
    """
    Generates a random move for the computer.
    Returns: A string ('rock', 'paper', or 'scissors').
    """
    # TODO: Member B writes code here
    return "rock" # Placeholder


def determine_winner(player_move, computer_move):
    """
    Compares the two moves to decide the winner.
    Args:
        player_move (str): The player's move.
        computer_move (str): The computer's move.
    Returns: 
        'player' (if player wins), 
        'computer' (if computer wins), 
        'tie' (if it's a draw).
    """
    # TODO: Member B writes code here using if/elif/else
    return "tie" # Placeholder


# ==========================================
# 🟠 MEMBER C: Game Manager (Main Loop)
# ==========================================
def play_game():
    """
    The main function that runs the game loop.
    It calls the functions from Member A and Member B.
    """
    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        # 1. Get moves
        # p_move = get_player_choice() (Call Member A's function)
        # c_move = get_computer_choice() (Call Member B's function)
        
        # 2. Judge the result
        # result = determine_winner(p_move, c_move) (Call Member B's function)
        
        # 3. Print the result and handle scoring
        # TODO: Member C writes the logic to show results and score
        
        # 4. Ask to play again
        # ...
        pass # Remove this when you start writing

if __name__ == "__main__":
    play_game()
