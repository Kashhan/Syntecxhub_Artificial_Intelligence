from maze import create_maze
from astar import astar_search
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate_search(maze, explored, path):
    rows = len(maze)
    cols = len(maze[0])

    grid = [[1 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                grid[r][c] = 0

    fig, ax = plt.subplots()

    def update(frame):
        r, c = explored[frame]
        grid[r][c] = 0.7
        ax.clear()
        ax.imshow(grid, cmap="gray")
        ax.set_title(f"Step {frame + 1}")

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(explored),
        interval=200,
        repeat=False
    )

    plt.show()

    if path:
        for r, c in path:
            grid[r][c] = 0.4

        plt.imshow(grid, cmap="gray")
        plt.title("Final Shortest Path")
        plt.show()


def main():
    maze, start, goal = create_maze()
    path, explored = astar_search(maze, start, goal)

    if path:
        print("Shortest path found")
        print(path)
        animate_search(maze, explored, path)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
