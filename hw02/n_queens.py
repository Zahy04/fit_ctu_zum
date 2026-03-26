import pygame
import sys
import random
import math
import numpy as np


def get_score(board):
    n = len(board)
    horizontal_score = n - len(set(board))
    
    diag1_score = n - len(set(board[i] - i for i in range(n)))
    diag2_score = n - len(set(board[i] + i for i in range(n)))
        
    return - (horizontal_score + diag1_score + diag2_score) * 10


def propability_function(new_score, old_score, t):
    if t < 1e-10:
        return 0
    return math.exp((new_score - old_score) / t)


def main():
    pygame.init()
    

    initial_t = 10
    t = initial_t
    current_score = 0
    
    board_size = 600
    sidebar_width = 300
    window_width = board_size + sidebar_width
    window_height = board_size
    queen_img_original = pygame.image.load("queen.png")
    
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("N-Queens - Simulované žíhání")

    font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 24)
    info_font = pygame.font.Font(None, 28) 
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (220, 220, 220)
    DARK_GRAY = (170, 170, 170)
    GREEN = (118, 190, 118)
    RED = (200, 50, 50)
    LIGHT_BOARD = (238, 238, 210)
    DARK_BOARD = (118, 150, 86)

    BLUE_ACTIVE = pygame.Color('dodgerblue2')

    n = 8
    input_text = str(n)
    input_active = False

    queens = [] 
    app_state = "SETUP" 
    
    clock = pygame.time.Clock()
    update_delay = 10 
    last_update_time = pygame.time.get_ticks()

    btn_minus = pygame.Rect(620, 100, 40, 40)
    input_rect = pygame.Rect(665, 100, 60, 40)
    btn_plus = pygame.Rect(730, 100, 40, 40)
    btn_play = pygame.Rect(625, 500, 150, 60)

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.collidepoint(event.pos):
                    if app_state == "SETUP" or app_state == "SOLVED":
                        app_state = "SOLVING"
                        queens = [random.randint(0, n - 1) for _ in range(n)]
                        t = initial_t
                        current_score = get_score(queens) 
 
                    else:
                        app_state = "SETUP"
                        queens = []
                        current_score = 0

                if app_state == "SETUP" or app_state == "SOLVED":
                    if input_rect.collidepoint(event.pos):
                        input_active = True
                    else:
                        input_active = False

                    if btn_minus.collidepoint(event.pos):
                        if n > 1:
                            n -= 1
                            input_text = str(n)
                    elif btn_plus.collidepoint(event.pos):
                        if n < 100:
                            n += 1
                            input_text = str(n)

            if event.type == pygame.KEYDOWN and (app_state == "SETUP" or app_state == "SOLVED"):
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isnumeric():
                        if len(input_text) < 3:
                            input_text += event.unicode
                    
                    try:
                        n = max(1, int(input_text))
                    except ValueError:
                        n = 1

        if app_state == "SOLVING":
            if current_time - last_update_time > update_delay:

                current_score = get_score(queens)
                
                if current_score == 0:
                    app_state = "SOLVED" 
                else:
                    changed_idx, changed_to = random.randint(0, n-1), random.randint(0, n-1)
                    new_queens = queens.copy()
                    new_queens[changed_idx] = changed_to
                    new_score = get_score(new_queens)
                    
                    if new_score > current_score:
                        queens = new_queens
                    elif propability_function(new_score, current_score, t) > random.random():
                        queens = new_queens
                        
                    t *= 0.998
                
                last_update_time = current_time

        screen.fill(WHITE)
        square_size = board_size // n
        queen_size = int(square_size * 0.8)
        queen_img_scaled = pygame.transform.smoothscale(queen_img_original, (queen_size, queen_size))
        for row in range(n):
            for col in range(n):
                color = LIGHT_BOARD if (row + col) % 2 == 0 else DARK_BOARD
                x = col * square_size
                y = row * square_size
                pygame.draw.rect(screen, color, (x, y, square_size, square_size))

        if len(queens) == n:
            for col in range(n):
                row = queens[col]
                img_x = col * square_size + (square_size - queen_size) // 2
                img_y = row * square_size + (square_size - queen_size) // 2
                screen.blit(queen_img_scaled, (img_x, img_y))

        sidebar_rect = pygame.Rect(board_size, 0, sidebar_width, window_height)
        pygame.draw.rect(screen, GRAY, sidebar_rect)
        pygame.draw.line(screen, BLACK, (board_size, 0), (board_size, window_height), 2)

        title_surf = font.render("Nastavení", True, BLACK)
        screen.blit(title_surf, (640, 30))

        n_label = small_font.render("Velikost N:", True, BLACK)
        screen.blit(n_label, (655, 80))

        btn_color = DARK_GRAY if app_state == "SETUP" or app_state == "SOLVED" else GRAY
        pygame.draw.rect(screen, btn_color, btn_minus, border_radius=5)
        pygame.draw.rect(screen, btn_color, btn_plus, border_radius=5)
        
        screen.blit(font.render("-", True, BLACK), font.render("-", True, BLACK).get_rect(center=btn_minus.center))
        screen.blit(font.render("+", True, BLACK), font.render("+", True, BLACK).get_rect(center=btn_plus.center))

        box_color = BLUE_ACTIVE if input_active and (app_state == "SETUP" or app_state == "SOLVED") else BLACK
        pygame.draw.rect(screen, box_color, input_rect, 2, border_radius=3)
        text_surf = font.render(input_text, True, BLACK)
        screen.blit(text_surf, text_surf.get_rect(center=input_rect.center))

        pygame.draw.line(screen, DARK_GRAY, (board_size + 20, 180), (window_width - 20, 180), 2)
        
        info_title = small_font.render("Stav výpočtu:", True, BLACK)
        screen.blit(info_title, (645, 200))


        display_score = 0 if app_state == "SOLVED" else current_score

        score_color = GREEN if display_score == 0 and app_state != "SETUP" else BLACK
        score_text = info_font.render(f"Skóre: {display_score}", True, score_color)
        screen.blit(score_text, (620, 240))

        temp_text = info_font.render(f"Teplota (T): {t:.2f}", True, BLACK)
        screen.blit(temp_text, (620, 280))

        if app_state == "SETUP" or app_state == "SOLVED":
            pygame.draw.rect(screen, GREEN, btn_play, border_radius=8)
            play_surf = font.render("PLAY", True, BLACK)
        else:
            pygame.draw.rect(screen, RED, btn_play, border_radius=8)
            play_surf = font.render("STOP", True, BLACK)
            
        screen.blit(play_surf, play_surf.get_rect(center=btn_play.center))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()