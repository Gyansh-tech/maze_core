class Robot:
    """The robot object provides the essential mechanisms required to simulate a robot which can traverse a maze."""
    def __init__(self,maze,x=0,y=0,orientation = "North"):
        self.coordinates = {"x":x,"y":y}
        self.orientation = orientation
        self.maze = maze
        self.currentCell = self.maze.maze[y][x]
        self.accessible_neighbours = {}
        self.accessible_directions = []
        self.start_cell = self.maze.maze[y][x]
        ##Initializes the end cell to the last cell.
        self.path = []
        self.update_robot()

    def update_robot(self):
        """Internal method that updates the current cell and accessible neighbours for the robot."""
        self.currentCell = self.maze.maze[self.coordinates["y"]][self.coordinates["x"]]
        self.accessible_neighbours = self.currentCell.accessible_neighbours
        self.accessible_directions = self.currentCell.accessible_directions

    def go_direction(self,direction):
        """Moves the robot in a specific direction."""
        if direction == "North":
            self.coordinates["y"] += 1
            self.path.append("North")
        elif direction == "South":
            self.coordinates["y"] -= 1
            self.path.append("South")
        elif direction == "East":
            self.coordinates["x"] += 1
            self.path.append("East")
        elif direction == "West":
            self.coordinates["x"] -= 1
            self.path.append("West")
        self.update_robot()
