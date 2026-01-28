def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, maze):
    rows = len(maze)
    cols = len(maze[0])
    r, c = position

    neighbors = []

    moves = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]

    for nr, nc in moves:
        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] != 1:
                neighbors.append((nr, nc))

    return neighbors
