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
    explored_frames = []

    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        explored_frames.append(current_node.position)

        if current_node == goal_node:
            path = reconstruct_path(current_node)
            return path, explored_frames

        for pos in get_neighbors(current_node.position, maze):
            neighbor = Node(pos, current_node)

            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                open_list.append(neighbor)

    return None, explored_frames


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g >= node.g:
            return False
    return True


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]
