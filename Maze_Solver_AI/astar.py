from utils import manhattan_distance, get_neighbors


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar_search(maze, start, goal):
    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node == goal_node:
            return reconstruct_path(current_node)

        neighbors = get_neighbors(current_node.position, maze)

        for next_position in neighbors:
            neighbor = Node(next_position, current_node)

            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                open_list.append(neighbor)

    return None


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g >= node.g:
            return False
    return True


def reconstruct_path(node):
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return path[::-1]
