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
    surface.fill(COLOR_BG)  # Clear screen

    # Draw Title
    title = font_big.render("Rock Paper Scissors", True, COLOR_TEXT)
    surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

    # Helper: map move -> image
    move_to_img = {
        "rock": img_rock,
        "paper": img_paper,
        "scissors": img_scissors
    }

    if game_state == "WAITING":
        # Draw the 3 choice images
        surface.blit(img_rock, rect_rock)
        surface.blit(img_paper, rect_paper)
        surface.blit(img_scissors, rect_scissors)

        # Prompt text
        prompt = font_small.render("Choose your move", True, COLOR_TEXT)
        surface.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 320))

        # Optional labels above icons
        lbl_rock = font_small.render("Rock", True, COLOR_TEXT)
        lbl_paper = font_small.render("Paper", True, COLOR_TEXT)
        lbl_scissors = font_small.render("Scissors", True, COLOR_TEXT)

        surface.blit(lbl_rock, (rect_rock.centerx - lbl_rock.get_width() // 2, rect_rock.y - 35))
        surface.blit(lbl_paper, (rect_paper.centerx - lbl_paper.get_width() // 2, rect_paper.y - 35))
        surface.blit(lbl_scissors, (rect_scissors.centerx - lbl_scissors.get_width() // 2, rect_scissors.y - 35))

    elif game_state == "SHOWING":
        # Player image (left)
        if p_move in move_to_img:
            surface.blit(move_to_img[p_move], (150, 250))

        # Computer image (right)
        if c_move in move_to_img:
            surface.blit(move_to_img[c_move], (500, 250))

        # Labels
        p_label = font_small.render("You", True, COLOR_TEXT)
        c_label = font_small.render("Computer", True, COLOR_TEXT)
        surface.blit(p_label, (150 + 75 - p_label.get_width() // 2, 210))
        surface.blit(c_label, (500 + 75 - c_label.get_width() // 2, 210))

        # Result text in center
        if result_text == "player":
            msg = "You Win!"
        elif result_text == "computer":
            msg = "You Lose!"
        else:
            msg = "Tie!"

        result_render = font_big.render(msg, True, COLOR_TEXT)
        surface.blit(result_render, (SCREEN_WIDTH // 2 - result_render.get_width() // 2, 120))

        # Small hint
        hint = font_small.render("Returning to selection...", True, COLOR_TEXT)
        surface.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 190))

    # ✅ Flaticon Attribution (visible credit in-game)
    credit_font = pygame.font.SysFont("Arial", 16)
    credit = credit_font.render("Icons by Freepik - Flaticon.com", True, (180, 180, 180))
    surface.blit(credit, (10, SCREEN_HEIGHT - 25))

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

            if event.type == pygame.MOUSEBUTTONDOWN and state == "WAITING":
                clicked = False
                
                if rect_rock.collidepoint(event.pos):
                    player_choice = "rock"
                    clicked = True
                elif rect_paper.collidepoint(event.pos):
                    player_choice = "paper"
                    clicked = True
                elif rect_scissors.collidepoint(event.pos):
                    player_choice = "scissors"
                    clicked = True
                
                if clicked:
                    cpu_choice = get_computer_move()
                    result = get_winner(player_choice, cpu_choice)
                    
                    print(f"玩家: {player_choice} vs 电脑: {cpu_choice} -> 结果: {result}")
                    
                    state = "SHOWING"
                    timer_start = pygame.time.get_ticks()

        if state == "SHOWING":
            current_time = pygame.time.get_ticks()
            if current_time - timer_start > 2000:
                state = "WAITING"
        
        draw_scene(screen, state, result, player_choice, cpu_choice)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()