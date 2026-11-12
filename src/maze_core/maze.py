from .MazeCell import MazeCell
from .MazeCursor import MazeCursor
import random

class Maze:
    """This class provides the following Methods:
    ,generate_random_maze()
    ,init_empty_maze()
    ,calculate_neighbours(cell)
    ,return_coordinates_neighbour(cell,direction)
    ,check_if_edge(cell)
    ,calculate_accessible neighbours(cell)
    ,update_all_neighbours()
    ,update_all_accessible_neighbours()
    ,update_all_unvisited_data()

    . Note: This class relies on the MazeCell class, as all cells are stored as MazeCell objects.
    """

    #Maze Initialization
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.maze = []
        self.init_empty_maze()

    def init_empty_maze(self):
        """Initializes an empty maze with cell objects in an order such
        that the x and y coordinates of the cell objects correspond perfectly
        with the coordinates in the 2d list. Note that the coordinates in the 2d list are
        in the form [row][cell] or [y][x]"""
        # Initialize empty rows
        for row in range(self.height):
            self.maze.append([])

        ##Assigning cells to each row:
        for row in range(self.height):
            for cell in range(self.width):
                self.maze[row].append(MazeCell(x=cell,y=row))
                self.check_if_edge(self.maze[row][cell])

        #Update attributes of each cell associated with their neighbours
        self.update_all_neighbours()
        self.update_all_accessible_neighbours()
        self.update_all_unvisited_data()







    ##Methods to update the maze and the cell attributes
    def calculate_neighbours(self, cell):
        # cell.clear_neighbours()
        """Updates the neighbours attribute for each cell."""
        if cell.top_edge and cell.right_edge:
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
        elif cell.top_edge and cell.left_edge:
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
        elif cell.bottom_edge and cell.right_edge:
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
        elif cell.bottom_edge and cell.left_edge:
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
        elif cell.top_edge:
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")
        elif cell.bottom_edge:
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")
        elif cell.left_edge:
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
        elif cell.right_edge:
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
        else:
            cell.neighbours["North"] = self.return_coordinates_neighbour(cell, "North")
            cell.neighbours["South"] = self.return_coordinates_neighbour(cell, "South")
            cell.neighbours["East"] = self.return_coordinates_neighbour(cell, "East")
            cell.neighbours["West"] = self.return_coordinates_neighbour(cell, "West")

    def return_coordinates_neighbour(self, cell, direction):
        """Returns the coordinates of a neighbour in a particular direction."""
        if direction == "North":
            return self.maze[cell.coordinates["y"] + 1][cell.coordinates["x"]]
        elif direction == "South":
            return self.maze[cell.coordinates["y"] - 1][cell.coordinates["x"]]
        elif direction == "East":
            return self.maze[cell.coordinates["y"]][cell.coordinates["x"] + 1]
        elif direction == "West":
            return self.maze[cell.coordinates["y"]][cell.coordinates["x"] - 1]
        else:
            return self.maze[cell.coordinates["y"]][cell.coordinates["x"]]

    def check_if_edge(self, cell):
        """Updates the edge attributes for each cell object, and assigns the cell the edge walls it needs to have"""
        if cell.coordinates["x"] == 0:
            cell.left_edge = True
            cell.west_wall = True
        if cell.coordinates["x"] == self.width - 1:
            cell.right_edge = True
            cell.east_wall = True
        if cell.coordinates["y"] == 0:
            cell.bottom_edge = True
            cell.south_wall = True
        if cell.coordinates["y"] == self.height - 1:
            cell.top_edge = True
            cell.north_wall = True

    @staticmethod
    def calculate_accessible_neighbours(cell):
        """Updates the accessible_neighbours attribute for each cell by checking accessibility of
        neighbours based on walls"""
        if cell.neighbours["North"] is not None:
            if not cell.neighbours["North"].south_wall:
                cell.accessible_neighbours["North"] = cell.neighbours["North"]
                cell.accessible_directions.append("North")
        if cell.neighbours["South"] is not None:
            if not cell.neighbours["South"].north_wall:
                cell.accessible_neighbours["South"] = cell.neighbours["South"]
                cell.accessible_directions.append("South")
        if cell.neighbours["East"] is not None:
            if not cell.neighbours["East"].west_wall:
                cell.accessible_neighbours["East"] = cell.neighbours["East"]
                cell.accessible_directions.append("East")
        if cell.neighbours["West"] is not None:
            if not cell.neighbours["West"].east_wall:
                cell.accessible_neighbours["West"] = cell.neighbours["West"]
                cell.accessible_directions.append("West")

    def update_all_neighbours(self):
        """Updates all the neighbours"""
        for row in self.maze:
            for cell in row:
                self.calculate_neighbours(cell)

    def update_all_accessible_neighbours(self):
        """Updates all accessible neighbours"""
        for row in self.maze:
            for cell in row:
                self.calculate_accessible_neighbours(cell)

    def update_all_unvisited_data(self):
        """Updates the unvisited_neighbours and unvisited_directions attributes of each cell."""
        for row in self.maze:
            for cell in row:
                cell.update_unvisited_neighbours_directions()







    #Methods to generate random maze
    def generate_random_maze(self):
        """Generates a random maze using Depth First Search. This directly updates the wall attributes of each cell"""
        ##Initializing the process
        cursor = MazeCursor()
        cursor.go_to(random.randint(0,self.width-1), random.randint(0,self.height-1))
        self.update_current_cursor_status(cursor)
        while cursor.stack:
            print(cursor.currentCell.coordinates)
            if cursor.currentCell.is_unvisited_direction():
                ##Direction choice will always have a direction in this case
                direction_choice = random.choice(self.return_unvisited_direction(cursor))
                cursor.carve_direction(direction_choice)
                self.update_current_cursor_status(cursor)
            else:
                while not cursor.currentCell.is_unvisited_direction():
                    cursor.stack.pop()
                    if cursor.stack:
                        cursor.go_to(cursor.stack[-1].coordinates["x"], cursor.stack[-1].coordinates["y"])
                        cursor.currentCell = self.maze[cursor.y][cursor.x]
                        cursor.currentCell.update_unvisited_neighbours_directions()
                    else:
                        break

        #Makes sure each cell's accessible neighbours are updated to account for the generated maze.
        self.update_all_accessible_neighbours()
        print("Maze has been generated")

    @staticmethod
    def return_unvisited_direction(cursor):
        """Returns the unvisited directions for a specific cell as a list from which a random choice can be made"""
        unvisited_directions = []
        ##Updates this list
        for direction in cursor.currentCell.unvisited_directions:
            if cursor.currentCell.unvisited_directions[direction]:
                unvisited_directions.append(direction)
        return unvisited_directions


    def update_current_cursor_status(self, cursor):
        """Updates attributes of the cursor to the latest data. Also recalculates unvisited data for all cells in the maze"""
        cursor.currentCell = self.maze[cursor.y][cursor.x]
        cursor.stack.append(cursor.currentCell)
        cursor.currentCell.visited = True
        cursor.currentCell.update_unvisited_neighbours_directions()
        self.update_all_unvisited_data()

