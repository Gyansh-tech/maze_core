class MazeCell:
    """Each cell in the maze is stored as a Maze Cell Object. Some key attributes for the user include:
    north_wall(boolean)
    south_wall(boolean)
    east_wall(boolean)
    west_wall(booelan)
    coordinates = {"x":x,"y":y}(dictionary)
    left_edge(boolean)
    right_edge(boolean)
    top_edge(boolean)
    bottom_edge(boolean)
    neighbours = {"North":MazeCell,"South":MazeCell,"East",MazeCell,"West":MazeCell}
    accessible_neighbours = {"North":MazeCell,"South":MazeCell,"East",MazeCell,"West":MazeCell}
    value(any)
    visited(boolean)

    Other attributes used in maze generation:
    unvisited_neighbours
    unvisited_directions
    visited(needs to be reset before the user uses it)

    """

    def __init__(self,x,y,north_wall = True, south_wall = True, east_wall = True, west_wall = True):
        #Essential information for each cell.
        self.north_wall = north_wall
        self.south_wall = south_wall
        self.east_wall = east_wall
        self.west_wall = west_wall
        self.coordinates = {"x":x,"y":y}
        ##Attribute that can be used as to the programmers discretion to assign a value or cost to the cell
        self.value = 0


        #Stores if the cell is an edge of the maze.
        self.left_edge = False
        self.right_edge = False
        self.top_edge = False
        self.bottom_edge = False


        #Stores neighbors and accessible neighbors - Relative to the current cell.
        self.neighbours = {"North":None, "South":None, "East":None, "West":None}
        self.accessible_neighbours = {"North":None,"South":None,"East":None,"West":None}

        #Attributes required for generation through DFS
        self.visited = False
        self.unvisited_neighbours = {"North":None,"South":None,"East":None,"West":None}
        self.unvisited_directions = {"North":True,"South":True, "East": True, "West": True}

    def clear_data(self):
        """Clears the visited, value, unvisited_neighbours, unvisited_directions attributes."""
        self.visited = False
        self.value = 0
        self.unvisited_neighbours = {"North":None,"South":None,"East":None,"West":None}
        self.unvisited_directions = {"North":True,"South":True, "East": True, "West": True}


    def update_unvisited_direction(self):
        """Directly updates all the unvisited directions by checking all the unvisited neighbours"""
        for direction in self.unvisited_neighbours:
            if self.unvisited_neighbours[direction] is not None:
                self.unvisited_directions[direction] = True
            else:
                self.unvisited_directions[direction] = False

    def calculate_unvisited_neighbours(self):
        """Calculates all unvisited neighbours from the neighbours of a cell. This accounts for cells on the edge"""
        #Update unvisited_neighbours in the North
        if self.neighbours["North"] is not None:
            if not self.neighbours["North"].visited:
                self.unvisited_neighbours["North"] = self.neighbours["North"]
            else:
                self.unvisited_neighbours["North"] = None

        #Update unvisited_neighbours in the South:
        if self.neighbours["South"] is not None:
            if not self.neighbours["South"].visited:
                self.unvisited_neighbours["South"] = self.neighbours["South"]
            else:
                self.unvisited_neighbours["South"] = None

        #Update unvisited_neighbours in the East:
        if self.neighbours["East"] is not None:
            if not self.neighbours["East"].visited:
                self.unvisited_neighbours["East"] = self.neighbours["East"]
            else:
                self.unvisited_neighbours["East"] = None

        #Update unvisited_neighbours in the West:
        if self.neighbours["West"] is not None:
            if not self.neighbours["West"].visited:
                self.unvisited_neighbours["West"] = self.neighbours["West"]
            else:
                self.unvisited_neighbours["West"] = None

    def update_unvisited_neighbours_directions(self):
        """Updates the unvisited neighbours and unvisited directions attributes"""
        self.calculate_unvisited_neighbours()
        self.update_unvisited_direction()

    def is_unvisited_direction(self):
        """Returns if a direction is unvisited by accessing the dictionary of unvisited neighbours"""
        for direction in self.unvisited_directions:
            if self.unvisited_directions[direction]:
                return True
        return False
