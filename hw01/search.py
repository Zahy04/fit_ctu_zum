import sys
import random
import heapq
import time

def random_search(labyrinth, start, end, sleep_time):
    queue = []
    lines = 100
    queue.append(start)
    D = {start : 0}
    P = {start : None}
    visited = {start}
    while (queue):
        index = random.randrange(len(queue))
        (current_x, current_y) = queue.pop(index)
        if (current_x, current_y) == end: 
            print(f"\033[{lines}A", end="")  
            current = (current_x, current_y)
            path = []
            while current is not None:
                path.append(current)
                current = P[current]
            for (x, y) in path: 
                if labyrinth[x][y] == '#': labyrinth[x][y] = 'o' 
                
            for x, column in enumerate(labyrinth):
                for y, pixel in enumerate(column):
                    if (x,y)  == start:
                        print("S", end='')
                    elif (x,y) == end:
                        print("E", end='')
                    elif pixel == 'o':
                        print("\033[92mo\033[0m", end='')
                    else: print(pixel, end='')
                print("")
            
            legend = '''---------------------------------------
S Start
E End
# Opened node
o Path
X Wall
space Fresh node
---------------------------------------'''
            print(legend)
            print(f"Nodes expanded: {len(visited)}")
            print(f"Path length: {D[end]}")
            return
            
            
        for (change_x, change_y) in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = (current_x + change_x , current_y + change_y)
            if (labyrinth[current_x + change_x][current_y + change_y] == ' ' and 
                new not in visited):
                labyrinth[current_x + change_x][current_y + change_y] = '#'
                queue.append(new)
                visited.add(new)
                D[new] = D[(current_x, current_y)] + 1
                P[new] = (current_x, current_y)
        print(f"\033[{lines}A", end="")       
        for x, column in enumerate(labyrinth):
            for y, pixel in enumerate(column):
                if (x,y) == start:
                    print("S", end='')
                elif (x,y) == end:
                    print("E", end='')
                else: print(pixel, end='')
            print("")
        time.sleep(sleep_time)
    print("No path found!")

def dfs_search(labyrinth, start, end, sleep_time):
    queue = []
    lines = 100
    queue.append(start)
    D = {start : 0}
    P = {start : None}
    visited = {start}
    while (queue):
        (current_x, current_y) = queue.pop(-1)
        if (current_x, current_y) == end: 
            print(f"\033[{lines}A", end="")  
            current = (current_x, current_y)
            path = []
            while current is not None:
                path.append(current)
                current = P[current]
            for (x, y) in path: 
                if labyrinth[x][y] == '#': labyrinth[x][y] = 'o' 
                
            for x, column in enumerate(labyrinth):
                for y, pixel in enumerate(column):
                    if (x,y)  == start:
                        print("S", end='')
                    elif (x,y) == end:
                        print("E", end='')
                    elif pixel == 'o':
                        print("\033[92mo\033[0m", end='')
                    else: print(pixel, end='')
                print("")
            
            legend = '''---------------------------------------
S Start
E End
# Opened node
o Path
X Wall
space Fresh node
---------------------------------------'''
            print(legend)
            print(f"Nodes expanded: {len(visited)}")
            print(f"Path length: {D[end]}")
            return
            
            
        for (change_x, change_y) in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = (current_x + change_x , current_y + change_y)
            if (labyrinth[current_x + change_x][current_y + change_y] == ' ' and 
                new not in visited):
                labyrinth[current_x + change_x][current_y + change_y] = '#'
                queue.append(new)
                visited.add(new)
                D[new] = D[(current_x, current_y)] + 1
                P[new] = (current_x, current_y)
        print(f"\033[{lines}A", end="")       
        for x, column in enumerate(labyrinth):
            for y, pixel in enumerate(column):
                if (x,y) == start:
                    print("S", end='')
                elif (x,y) == end:
                    print("E", end='')
                else: print(pixel, end='')
            print("")
        time.sleep(sleep_time)
    print("No path found!")

def bfs_search(labyrinth, start, end, sleep_time):
    lines = 100
    queue = []
    queue.append(start)
    D = {start : 0}
    P = {start : None}
    visited = {start}
    while (queue):
        (current_x, current_y) = queue.pop(0)
        if (current_x, current_y) == end: 
            print(f"\033[{lines}A", end="")  
            current = (current_x, current_y)
            path = []
            while current is not None:
                path.append(current)
                current = P[current]
            for (x, y) in path: 
                if labyrinth[x][y] == '#': labyrinth[x][y] = 'o' 
                
            for x, column in enumerate(labyrinth):
                for y, pixel in enumerate(column):
                    if (x,y)  == start:
                        print("S", end='')
                    elif (x,y) == end:
                        print("E", end='')
                    elif pixel == 'o':
                        print("\033[92mo\033[0m", end='')
                    else: print(pixel, end='')
                print("")
            
            legend = '''---------------------------------------
S Start
E End
# Opened node
o Path
X Wall
space Fresh node
---------------------------------------'''
            print(legend)
            print(f"Nodes expanded: {len(visited)}")
            print(f"Path length: {D[end]}")
            return
            
            
        for (change_x, change_y) in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = (current_x + change_x , current_y + change_y)

            if (labyrinth[current_x + change_x][current_y + change_y] == ' ' and 
                new not in visited):
                visited.add(new)
                labyrinth[current_x + change_x][current_y + change_y] = '#'
                queue.append(new)
                D[new] = D[(current_x, current_y)] + 1
                P[new] = (current_x, current_y)
                
        print(f"\033[{lines}A", end="")       
        for x, column in enumerate(labyrinth):
            for y, pixel in enumerate(column):
                if (x,y) == start:
                    print("S", end='')
                elif (x,y) == end:
                    print("E", end='')
                else: print(pixel, end='')
            print("")
        time.sleep(sleep_time)
    print("No path found!")
        
def heuristic(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])    
    

def greedy_search(labyrinth, start, end, sleep_time):
    lines = 100
    queue = []
    heapq.heappush(queue, (0, start))
    D = {start : 0}
    P = {start : None}
    visited = {start}
    while (queue):
        priority, (current_x, current_y) = heapq.heappop(queue)
        if (current_x, current_y) == end: 
            print(f"\033[{lines}A", end="")  
            current = (current_x, current_y)
            path = []
            while current is not None:
                path.append(current)
                current = P[current]
            for (x, y) in path: 
                if labyrinth[x][y] == '#': labyrinth[x][y] = 'o' 
                
            for x, column in enumerate(labyrinth):
                for y, pixel in enumerate(column):
                    if (x,y)  == start:
                        print("S", end='')
                    elif (x,y) == end:
                        print("E", end='')
                    elif pixel == 'o':
                        print("\033[92mo\033[0m", end='')
                    else: print(pixel, end='')
                print("")
            
            legend = '''---------------------------------------
S Start
E End
# Opened node
o Path
X Wall
space Fresh node
---------------------------------------'''
            print(legend)
            print(f"Nodes expanded: {len(visited)}")
            print(f"Path length: {D[end]}")
            return
            
            
        for (change_x, change_y) in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = (current_x + change_x , current_y + change_y)
            if (labyrinth[current_x + change_x][current_y + change_y] == ' ' and 
                new not in visited):
                visited.add(new)
                labyrinth[current_x + change_x][current_y + change_y] = '#'
                h = heuristic(new, end)
                heapq.heappush(queue, (h, new))
                D[new] = D[(current_x, current_y)] + 1
                P[new] = (current_x, current_y)
        print(f"\033[{lines}A", end="")       
        for x, column in enumerate(labyrinth):
            for y, pixel in enumerate(column):
                if (x,y) == start:
                    print("S", end='')
                elif (x,y) == end:
                    print("E", end='')
                else: print(pixel, end='')
            print("")
        time.sleep(sleep_time)
    print("No path found!")

def a_star_search(labyrinth, start, end, sleep_time):
    lines = 100
    queue = []
    heapq.heappush(queue, (0, start)) 
    D = {start: 0}
    P = {start: None}
    
    while queue:
        priority, (current_x, current_y) = heapq.heappop(queue)

        if (current_x, current_y) == end:
            print(f"\033[{lines}A", end="")  
            current = (current_x, current_y)
            path = []
            while current is not None:
                path.append(current)
                current = P[current]

            for (x, y) in path:
                if labyrinth[x][y] == '#':
                    labyrinth[x][y] = 'o'

            print()
            for x, column in enumerate(labyrinth):
                for y, pixel in enumerate(column):
                    if (x, y) == start:
                        print("S", end='')
                    elif (x, y) == end:
                        print("E", end='')
                    elif pixel == 'o':
                        print("\033[92mo\033[0m", end='')
                    else:
                        print(pixel, end='')
                print("")
            
            legend = '''---------------------------------------
S Start
E End
# Opened node
o Path
X Wall
space Fresh node
---------------------------------------'''
            print(legend)
            print(f"Nodes expanded: {len(P)}")
            print(f"Path length: {D[end]}")
            return

        for (change_x, change_y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = current_x + change_x
            new_y = current_y + change_y
            new = (new_x, new_y)

            if labyrinth[new_x][new_y] == ' ' and new not in P:
                labyrinth[new_x][new_y] = '#'
                P[new] = (current_x, current_y)
                D[new] = D[(current_x, current_y)] + 1

                f = D[new] + heuristic(new, end)
                heapq.heappush(queue, (f, new))
                
        print(f"\033[{lines}A", end="")       
        for x, column in enumerate(labyrinth):
            for y, pixel in enumerate(column):
                if (x,y) == start:
                    print("S", end='')
                elif (x,y) == end:
                    print("E", end='')
                else: print(pixel, end='')
            print("")
        time.sleep(sleep_time)
    
    print("No path found!")



def search(labyritnh, start, end, algorithm, sleep_time):
    print("\033[2J\033[H", end="")
    if algorithm == 'random': random_search(labyritnh, start, end, sleep_time)
    if algorithm == 'dfs': dfs_search(labyritnh, start,       end, sleep_time)
    if algorithm == 'bfs': bfs_search(labyritnh, start,       end, sleep_time)
    if algorithm == 'greedy': greedy_search(labyritnh, start, end, sleep_time)
    if algorithm == 'a*': a_star_search(labyritnh, start,     end, sleep_time)
    




def main():
    
    algorithms = {'random', 'dfs', 'bfs', 'greedy', 'a*'}
    if len(sys.argv) < 2:
        print("Error: No filepath!")
        print("Usage: python search.py filepath search_algorithm sleep_time")
        print("search alghorithms: random, dfs, bfs, greedy, a*")
        return 
    
    if len(sys.argv) in {3,4}:
        algorithm = sys.argv[2]
        if algorithm not in algorithms:
            print(f"Error: {algorithm} is not implented!")
            print("Usage: python search.py filepath search_algorithm sleep_time")
            print("search alghorithms: random, dfs, bfs, greedy, a*")
            return
    sleep_time = 0.05
    if len(sys.argv) == 4:
        sleep_time = float(sys.argv[3])
    
    filepath = sys.argv[1]
    labyrinth = []
    with open(filepath) as file:
        for line in file:
            clean_line = line.strip()
            if clean_line.startswith("start"):
               s_line = clean_line.split()
               break 
            labyrinth.append(list(clean_line))
            
        start_y = int(s_line[1].replace(",", ""))
        start_x = int(s_line[2])
        start = (start_x, start_y)
        e_line = file.readline().split()
        end_y = int(e_line[1].replace(",", ""))
        end_x = int(e_line[2])
        end = (end_x, end_y)
    
    print("Labyrinth:\n")
    for x, column in enumerate(labyrinth):
        
        for y, pixel in enumerate(column):
            if x == start_x and y == start_y:
                print("S", end='')
            elif x == end_x and y == end_y:
                print("E", end='')
            else: print(pixel, end='')
        print("")
        
    
    search(labyrinth, start, end, algorithm, sleep_time)
        
    
           
           
       
if __name__ == "__main__" :
    main()
    