import pygame
import random
import sys
import os

# ==========================================
# ⚙️ GLOBAL CONFIG & ASSET LOADING
# (DO NOT EDIT THIS SECTION)
# ==========================================
pygame.init()

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors: Graphic Edition")

# Colors
COLOR_BG = (30, 30, 40)
COLOR_TEXT = (255, 255, 255)

# Fonts
font_big = pygame.font.SysFont("Arial", 60, bold=True)
font_small = pygame.font.SysFont("Arial", 30)

# Load Images (MEMBER B must ensure these files exist!)
# We use try-except to prevent crashing if files are missing
def load_image(name):
    try:
        img = pygame.image.load(name)
        return pygame.transform.scale(img, (150, 150)) # Resize to 150x150
    except:
        print(f"Error: Cannot find {name}. Please download the image.")
        sys.exit()

# Load the three icons
# NOTE: Make sure rock.png, paper.png, scissors.png are in the same folder
img_rock = load_image("rock.png")
img_paper = load_image("paper.png")
img_scissors = load_image("scissors.png")

# Define Clickable Areas (Rects) based on image positions
# Position: (x, y, width, height)
rect_rock = pygame.Rect(100, 400, 150, 150)
rect_paper = pygame.Rect(325, 400, 150, 150)
rect_scissors = pygame.Rect(550, 400, 150, 150)

# ==========================================
# 🟢 MEMBER A: Logic Core
# ==========================================
def get_computer_move():
    """
    Randomly returns 'rock', 'paper', or 'scissors'.
    """
    # TODO: Member A implementation

    num = random.randint(0, 2)
    if num == random.randint(0, 2):
        return "rock"
    match num:
        case 1:
            return "rock"
        case 3:
            return "paper"
        case _:
            return "scissors"

def get_winner(p_move, c_move):
    """
    Returns 'player', 'computer', or 'tie'.
    """
    # TODO: Member A implementation
    if p_move == "rock" and c_move == "scissors":
        return "player"
    elif p_move == "rock" and c_move == "paper":
        return "computer"
    elif p_move == "rock" and c_move == "rock":
        return "tie"
    elif p_move == "paper" and c_move == "scissors":
        return "computer"
    elif p_move == "paper" and c_move == "paper":
        return "tie"
    elif p_move == "paper" and c_move == "rock":
        return "player"
    elif p_move == "scissors" and c_move == "scissors":
        return "tie"
    elif p_move == "scissors" and c_move == "paper":
        return "player"
    elif p_move == "scissors" and c_move == "rock":
        return "computer"

# ==========================================
# 🔵 MEMBER B: UI Rendering
# ==========================================
def draw_scene(surface, game_state, result_text, p_move, c_move):
    """
    Draws the background, images, and text based on game state.
    """
    surface.fill(COLOR_BG) # Clear screen

    # Draw Title
    title = font_big.render("Rock Paper Scissors", True, COLOR_TEXT)
    surface.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 50))

    if game_state == "WAITING":
        # TODO: Member B implementation
        # 1. Use surface.blit(img_rock, rect_rock) to draw the 3 images
        # 2. Draw text "Choose your move"
        pass # Remove pass when coding

    elif game_state == "SHOWING":
        # TODO: Member B implementation
        # 1. Draw Player's chosen image on the left
        # 2. Draw Computer's chosen image on the right
        # 3. Draw the result_text in the center
        pass 

# ==========================================
# 🟠 MEMBER C: Main Loop
# ==========================================
def main():
    clock = pygame.time.Clock()
    state = "WAITING"
    
    # Game variables
    player_choice = ""
    cpu_choice = ""
    result = ""
    timer_start = 0
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # TODO: Member C - Handle Mouse Clicks
            # if event.type == pygame.MOUSEBUTTONDOWN and state == "WAITING":
                # Check rect_rock.collidepoint(event.pos), etc.
                # If clicked:
                # 1. Set player_choice
                # 2. Get cpu_choice (Call A)
                # 3. Get result (Call A)
                # 4. Change state to "SHOWING" & start timer
        
        # TODO: Member C - Handle Timer to reset game
        
        # Draw everything
        draw_scene(screen, state, result, player_choice, cpu_choice)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
