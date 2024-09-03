def shuffle(puz, x1, y1, x2, y2):
    if 0 <= x2 < len(puz) and 0 <= y2 < len(puz):
        temp_puz = [list(row) for row in puz]
        temp_puz[x1][y1], temp_puz[x2][y2] = temp_puz[x2][y2], temp_puz[x1][y1]
        return [tuple(row) for row in temp_puz]
    else:
        return None

def find(puz, x):
    for i in range(len(puz)):
        for j in range(len(puz)):
            if puz[i][j] == x:
                return i, j

def calculate_f_h(start, goal):
    h_value = 0
    for i in range(len(start)):
        for j in range(len(start)):
            if start[i][j] != goal[i][j] and start[i][j] != '_':
                h_value += 1
    return h_value, h_value + len(start)

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(row))

def generate_child(puz, level, direction):
    x, y = find(puz, '_')
    children = []

    if x > 0 and direction != 'D':
        new_puz = shuffle(puz, x, y, x - 1, y)
        if new_puz is not None:
            children.append((new_puz, level + 1, 'UP'))

    if x < len(puz) - 1 and direction != 'U':
        new_puz = shuffle(puz, x, y, x + 1, y)
        if new_puz is not None:
            children.append((new_puz, level + 1, 'DOWN'))

    if y > 0 and direction != 'R':
        new_puz = shuffle(puz, x, y, x, y - 1)
        if new_puz is not None:
            children.append((new_puz, level + 1, 'LEFT'))

    if y < len(puz[0]) - 1 and direction != 'L':
        new_puz = shuffle(puz, x, y, x, y + 1)
        if new_puz is not None:
            children.append((new_puz, level + 1, 'RIGHT'))

    return children

def a_start(start, goal):
    open_list = [(start, 0, '')]
    closed_list = []

    while open_list:
        open_list.sort(key=lambda x: calculate_f_h(x[0], goal)[1])

        cur, level, direction = open_list.pop(0)
        closed_list.append(cur)
        h_value, f_value = calculate_f_h(cur, goal)

        if h_value == 0:
            print("Goal state reached!")
            break

        print("Step:", level)
        best_child = None
        best_h_value = float('inf')

        for child, child_level, child_direction in generate_child(cur, level, direction):
            if child not in closed_list:
                h_value, _ = calculate_f_h(child, goal)
                if h_value < best_h_value:
                    best_child = child
                    best_h_value = h_value
                    best_direction = child_direction

        if best_child:
            print("Empty cell moved:", best_direction, '\n')
            print_puzzle(best_child)
            open_list.append((best_child, level + 1, best_direction))

def accept():
    puz = []
    for i in range(3):
        temp = input().split(" ")
        puz.append(temp)
    return [tuple(row) for row in puz]

def main():
    print("Enter the start state matrix")
    start = accept()
    print("Enter the goal state matrix")
    goal = accept()
    a_start(start, goal)

if __name__ == "__main__":
    main()