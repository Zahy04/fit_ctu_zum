import pygame
import sys
import os
import numpy as np

CELL_SIZE = 40
MARGIN = 1
SIDEBAR_WIDTH = 260

EMPTY, WALL, BOX, TARGET, PLAYER = 0, 1, 2, 3, 4

COLORS = {
    EMPTY: (248, 249, 250),      
    WALL: (43, 45, 66),          
    BOX: (208, 140, 96),         
    TARGET: (230, 57, 70),       
    PLAYER: (69, 123, 157),      
    "grid_bg": (206, 212, 218),  
    "ui_bg": (255, 255, 255),    
    "ui_text": (33, 37, 41),     
    "active": (237, 242, 244),   
    "hover": (241, 243, 245),    
    "btn": (42, 157, 143),       
    "btn_hover": (50, 175, 160),
    "input_bg": (241, 243, 245),
    "input_active": (226, 232, 240)
}

TOOL_NAMES = {
    EMPTY: "Guma (Smazat)",
    WALL: "Zeď (Wall)",
    BOX: "Krabice (Box)",
    TARGET: "Cíl (Target)",
    PLAYER: "Skladník (Player)"
}

def generate_objects(grid, targets, rows, cols):
    positions = ''
    boxes = ''
    box_counter = 0
    player_counter = 0
    player = ''
    targets_count = len(targets)
    invalid_input = ''
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != WALL:
                positions += f' pos{i}_{j}\n'
            if grid[i][j] == BOX:
                box_counter += 1
                boxes += f' box_{box_counter}\n'
            if grid[i][j] == PLAYER:
                player_counter += 1
                player += f' player_{player_counter}\n'
    if box_counter > targets_count :
        invalid_input = "THERE IS MORE BOXES THAN TARGETS"
    elif player_counter != 1:
        invalid_input = "THERE SHOULD BE EXACTLY ONE PLAYER"
        
    return positions, boxes, player, box_counter ,invalid_input

def in_box( i, j , rows, cols):
    return i >= 0 and i < rows and j >= 0 and j < cols

def generate_init_state(grid, targets, rows, cols):
    inline = ""
    connected = ""
    clear = ""
    at = ""
    box_counter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]  == WALL: continue

            if in_box(i-1, j , rows, cols) and in_box(i+1, j , rows, cols)  and grid[i-1][j] != WALL and grid[i+1][j] != WALL:
                inline += f'(inline pos{i-1}_{j} pos{i}_{j} pos{i+1}_{j}\n)'
                inline += f'(inline pos{i+1}_{j} pos{i}_{j} pos{i-1}_{j}\n)'

      
            if in_box(i, j-1 , rows, cols) and in_box(i, j+1 , rows, cols)  and grid[i][j-1] != WALL and grid[i][j+1] != WALL:
                inline += f'(inline pos{i}_{j-1} pos{i}_{j} pos{i}_{j+1}\n)'
                inline += f'(inline pos{i}_{j+1} pos{i}_{j} pos{i}_{j-1}\n)'
                
                
                
            
            for neigbors in ([0,1], [1,0], [-1,0], [0,-1]):
              neigbor = np.array([i,j]) + np.array(neigbors) 
              if in_box(neigbor[0], neigbor[1], rows, cols) and grid[neigbor[0]][neigbor[1]] != WALL:
                  connected += f'(connected pos{i}_{j} pos{neigbor[0]}_{neigbor[1]})\n'    
                  
                  
            if grid[i][j] in [EMPTY , TARGET]:
                clear += f'(clear pos{i}_{j})\n'
            if grid[i][j] == PLAYER:
                at += f'(at player_1 pos{i}_{j})\n'
            if grid[i][j] == BOX:
                box_counter += 1
                at += f'(at box_{box_counter} pos{i}_{j})\n'
    
    return inline + connected + clear + at

def generate_goal_state(grid, box_count, targets, rows, cols):
    goal = ""
    first = True
    for i in range(box_count):
        goal += "(or "
        for target in targets:
            goal += f"(at box_{i+1} pos{target[0]}_{target[1]})\n "
        goal += ')'
        
    return goal
    
    
            
def export_to_pddl(grid, targets, rows, cols, filename="problem.pddl"):
        
    positions, boxes, player, box_count ,invalid_input = generate_objects(grid, targets, rows, cols)
    if invalid_input:
        return invalid_input
    init = generate_init_state(grid, targets, rows, cols)
    goal = generate_goal_state(grid, box_count, targets, rows, cols)
    objects = f"""(:objects
    {positions} - position
    {player} - player
    {boxes} - box)"""
    init = f"""(:init
    {init})"""
    
    goal = f"""(:goal (and
    {goal}))"""
    
    problem_pddl = "(define (problem sokoban-level)\n  (:domain sokoban)\n" + objects + '\n' + init + '\n' + goal + '\n)'
    print(problem_pddl)
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(problem_pddl)
    return f"SUCCESFULLY COMPILED INTO FILE {filename}"
    







def draw_rounded_rect(surface, color, rect, radius=5, width=0):
    """Pomocná funkce pro hezčí obdélníky v UI."""
    pygame.draw.rect(surface, color, rect, width, border_radius=radius)



    

def main():
    pygame.init()

    image_worker = None
    image_box = None
    image_wall = None
    
    try:
        raw_worker = pygame.image.load("worker.png")
        image_worker = pygame.transform.scale(raw_worker, (CELL_SIZE, CELL_SIZE))
    except Exception as e:
        print(f"Upozornění: Nepodařilo se načíst worker.png ({e})")
        
    try:
        raw_box = pygame.image.load("box.jpg")
        image_box = pygame.transform.scale(raw_box, (CELL_SIZE, CELL_SIZE))
    except Exception as e:
        print(f"Upozornění: Nepodařilo se načíst box.jpg ({e})")

    try:
        raw_wall = pygame.image.load("wall.png")
        image_wall = pygame.transform.scale(raw_wall, (CELL_SIZE, CELL_SIZE))
    except Exception as e:
        print(f"Upozornění: Nepodařilo se načíst wall.png ({e})")
    
    rows, cols = 8, 8
    grid = [[EMPTY for _ in range(cols)] for _ in range(rows)]
    
    targets = set()
    current_tool = WALL
    
    input_rows = str(rows)
    input_cols = str(cols)
    active_input = None 

    def update_screen_size():
        w = cols * (CELL_SIZE + MARGIN) + MARGIN + SIDEBAR_WIDTH
        h = max(rows * (CELL_SIZE + MARGIN) + MARGIN, 560)
        return pygame.display.set_mode((w, h)), w, h

    screen, width, height = update_screen_size()
    pygame.display.set_caption("Sokoban Editor")
    
    font_title = pygame.font.SysFont("Segoe UI", 22, bold=True)
    font_main = pygame.font.SysFont("Segoe UI", 16)
    font_btn = pygame.font.SysFont("Segoe UI", 16, bold=True)

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        grid_w = cols * (CELL_SIZE + MARGIN)
        grid_h = rows * (CELL_SIZE + MARGIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if pygame.mouse.get_pressed()[0]: 
                if mx < grid_w and my < grid_h:
                    c, r = mx // (CELL_SIZE + MARGIN), my // (CELL_SIZE + MARGIN)
                    
                    if current_tool == EMPTY:
                        grid[r][c] = EMPTY
                        targets.discard((r, c))
                    
                    elif current_tool == WALL:
                        grid[r][c] = WALL
                        targets.discard((r, c))
                        
                    elif current_tool == TARGET:
                        targets.add((r, c))
                        if grid[r][c] == WALL:
                            grid[r][c] = EMPTY
                            
                    elif current_tool in (BOX, PLAYER):
                        grid[r][c] = current_tool

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mx > grid_w + 10:

                        for i in range(5):
                            if grid_w + 15 < mx < width - 15 and 60 + i*45 < my < 100 + i*45:
                                current_tool = i


                        if grid_w + 90 < mx < grid_w + 150:
                            if 330 < my < 365: active_input = 'rows'
                            elif 380 < my < 415: active_input = 'cols'
                        else:
                            active_input = None

                    if grid_w + 15 < mx < width - 15 and 440 < my < 482:
                        try:
                            rows, cols = int(input_rows), int(input_cols)
                            grid = [[EMPTY for _ in range(cols)] for _ in range(rows)]
                            targets.clear()
                            screen, width, height = update_screen_size()
                        except ValueError: pass

                    if grid_w + 15 < mx < width - 15 and 495 < my < 537:
                        print(export_to_pddl(grid, targets, rows, cols))

            if event.type == pygame.KEYDOWN and active_input:
                if event.key == pygame.K_BACKSPACE:
                    if active_input == 'rows': input_rows = input_rows[:-1]
                    else: input_cols = input_cols[:-1]
                elif event.unicode.isdigit():
                    if len(input_rows if active_input == 'rows' else input_cols) < 2:
                        if active_input == 'rows': input_rows += event.unicode
                        else: input_cols += event.unicode

        screen.fill(COLORS["grid_bg"])

        for r in range(rows):
            for c in range(cols):
                rect = [c*(CELL_SIZE+MARGIN)+MARGIN, r*(CELL_SIZE+MARGIN)+MARGIN, CELL_SIZE, CELL_SIZE]
                cell_type = grid[r][c]
                is_target = (r, c) in targets
                
                pygame.draw.rect(screen, COLORS[EMPTY], rect)

                if is_target:
                    pad = 10
                    pygame.draw.line(screen, COLORS[TARGET], (rect[0]+pad, rect[1]+pad), (rect[0]+CELL_SIZE-pad, rect[1]+CELL_SIZE-pad), 4)
                    pygame.draw.line(screen, COLORS[TARGET], (rect[0]+CELL_SIZE-pad, rect[1]+pad), (rect[0]+pad, rect[1]+CELL_SIZE-pad), 4)
                
                if cell_type == WALL:
                    if image_wall:
                        screen.blit(image_wall, (rect[0], rect[1]))
                    else:
                        pygame.draw.rect(screen, COLORS[WALL], rect)
                
                elif cell_type == BOX:
                    if image_box:
                        screen.blit(image_box, (rect[0], rect[1]))
                    else:
                        draw_rounded_rect(screen, COLORS[BOX], [rect[0]+4, rect[1]+4, CELL_SIZE-8, CELL_SIZE-8], 4)
                        pygame.draw.line(screen, (180, 110, 70), (rect[0]+8, rect[1]+8), (rect[0]+CELL_SIZE-8, rect[1]+CELL_SIZE-8), 2)
                        pygame.draw.line(screen, (180, 110, 70), (rect[0]+CELL_SIZE-8, rect[1]+8), (rect[0]+8, rect[1]+CELL_SIZE-8), 2)

                    if is_target:
                        pad = 8
                        pygame.draw.line(screen, (230, 57, 70), (rect[0]+pad, rect[1]+pad), (rect[0]+CELL_SIZE-pad, rect[1]+CELL_SIZE-pad), 3)
                        pygame.draw.line(screen, (230, 57, 70), (rect[0]+CELL_SIZE-pad, rect[1]+pad), (rect[0]+pad, rect[1]+CELL_SIZE-pad), 3)
                
                elif cell_type == PLAYER:
                    if image_worker:
                        screen.blit(image_worker, (rect[0], rect[1]))
                    else:
                        center = (rect[0] + CELL_SIZE//2, rect[1] + CELL_SIZE//2)
                        pygame.draw.circle(screen, COLORS[PLAYER], center, CELL_SIZE//3)

                    if is_target:
                        pad = 8
                        pygame.draw.line(screen, (230, 57, 70), (rect[0]+pad, rect[1]+pad), (rect[0]+CELL_SIZE-pad, rect[1]+CELL_SIZE-pad), 3)
                        pygame.draw.line(screen, (230, 57, 70), (rect[0]+CELL_SIZE-pad, rect[1]+pad), (rect[0]+pad, rect[1]+CELL_SIZE-pad), 3)

        pygame.draw.rect(screen, COLORS["ui_bg"], [grid_w, 0, SIDEBAR_WIDTH, height])
        pygame.draw.line(screen, (220, 220, 220), (grid_w, 0), (grid_w, height), 2)
        
        screen.blit(font_title.render("Nástroje", True, COLORS["ui_text"]), (grid_w + 15, 20))
        
        for i, name in TOOL_NAMES.items():
            rect = [grid_w + 15, 60 + i*45, SIDEBAR_WIDTH - 30, 38]
            
            is_hovered = rect[0] < mx < rect[0] + rect[2] and rect[1] < my < rect[1] + rect[3]
            if i == current_tool:
                draw_rounded_rect(screen, COLORS["active"], rect, 6)
                draw_rounded_rect(screen, (200, 210, 220), rect, 6, 1)
            elif is_hovered:
                draw_rounded_rect(screen, COLORS["hover"], rect, 6)
            
            screen.blit(font_main.render(name, True, COLORS["ui_text"]), (grid_w + 30, 68 + i*45))

        pygame.draw.line(screen, (230, 230, 230), (grid_w + 15, 295), (width - 15, 295), 1)
        screen.blit(font_title.render("Rozměry sítě", True, COLORS["ui_text"]), (grid_w + 15, 300))
        
        screen.blit(font_main.render("Řádky:", True, COLORS["ui_text"]), (grid_w + 15, 335))
        r_rect = [grid_w + 90, 330, 60, 32]
        r_color = COLORS["input_active"] if active_input == 'rows' else COLORS["input_bg"]
        draw_rounded_rect(screen, r_color, r_rect, 4)
        screen.blit(font_main.render(input_rows, True, COLORS["ui_text"]), (grid_w + 100, 335))
        
        screen.blit(font_main.render("Sloupce:", True, COLORS["ui_text"]), (grid_w + 15, 385))
        c_rect = [grid_w + 90, 380, 60, 32]
        c_color = COLORS["input_active"] if active_input == 'cols' else COLORS["input_bg"]
        draw_rounded_rect(screen, c_color, c_rect, 4)
        screen.blit(font_main.render(input_cols, True, COLORS["ui_text"]), (grid_w + 100, 385))

        btn1_rect = [grid_w + 15, 440, SIDEBAR_WIDTH - 30, 42]
        btn1_hovered = btn1_rect[0] < mx < btn1_rect[0] + btn1_rect[2] and btn1_rect[1] < my < btn1_rect[1] + btn1_rect[3]
        draw_rounded_rect(screen, COLORS["btn_hover"] if btn1_hovered else COLORS["btn"], btn1_rect, 8)
        btn1_text = font_btn.render("Změnit mapu", True, (255, 255, 255))
        screen.blit(btn1_text, (btn1_rect[0] + (btn1_rect[2] - btn1_text.get_width()) // 2, btn1_rect[1] + 10))

        btn2_rect = [grid_w + 15, 495, SIDEBAR_WIDTH - 30, 42]
        btn2_hovered = btn2_rect[0] < mx < btn2_rect[0] + btn2_rect[2] and btn2_rect[1] < my < btn2_rect[1] + btn2_rect[3]
        draw_rounded_rect(screen, (33, 118, 174) if btn2_hovered else (43, 138, 194), btn2_rect, 8)
        btn2_text = font_btn.render("Generovat PDDL", True, (255, 255, 255))
        screen.blit(btn2_text, (btn2_rect[0] + (btn2_rect[2] - btn2_text.get_width()) // 2, btn2_rect[1] + 10))

        pygame.display.flip()

if __name__ == "__main__":
    main()