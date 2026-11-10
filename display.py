import copy
import sys
from turtle import Turtle,Screen


class Display:
    """Provides the Display functionalities needed for visualizing maze data and robot data.
    The display object can use both, the console and turtle graphics in order to carry out visualizations.
    Methods for console: print_coordinates_map(),print_cost_map(),print_maze().
    Methods for turtle graphics:
    display_maze(), execute_screen()."""

    #Class attributes and setup:
    py_recursion_limit = 2000 #You can safely push it up to 20000 and print a 50 * 50 maze(that is 2500 cells)
    #All the attributes needed for print functionalities:

    print_cell_width = 10
    print_wall_width = 1
    print_total_width = print_cell_width + (2 * print_wall_width)
    print_cell_height = 3
    print_characters = {"side_wall":"|","Cell":"\u2008", "top_wall":"."} # Pipe and dot

    #All the turtle graphics attributes
    ##This is the offset from the left and top borders for the maze
    border_offset = 50

    def __init__(self,maze):
        """Creates a deepcopy of the maze and saves it to the object"""
        self.maze = maze
        ##Updating python's recursion limit:
        sys.setrecursionlimit(Display.py_recursion_limit)
        self.grid = copy.deepcopy(maze.maze)
        self.grid.reverse()
        #All the turtle graphics attributes
        self.turtle = Turtle()
        self.screen = Screen()
        self.screen.setup(1.0,1.0)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.turtle_cell_width = 0
        self.turtle_cell_height = 0

        ##Setting up the display:
        self.set_parameters()

        ##Setting the turtle home position:
        self.home_x = -(self.screen.window_width()/2) + Display.border_offset
        self.home_y = (self.screen.window_height()/2) - Display.border_offset


    ##All the print functionalities:
    def print_coordinates_map(self):
        """Prints a coordinate map of the maze."""
        for row in self.grid:
            print("\n")
            for cell in row:
                print(f"|| ({cell.coordinates["x"]},{cell.coordinates["y"]})", end=" || ")
            print("\n" + "_" * self.maze.width * 12, end="_")

    def print_cost_map(self):
        """Prints a coordinate map of the maze."""
        for row in self.grid:
            print("\n")
            for cell in row:
                print(f"|| ({cell.value})", end=" || ")
            print("\n" + "_" * self.maze.width * 12, end="_")

    ##Print W.R.T to the cells.
    def print_row(self,row_number):
        """Prints a row in the maze at the specified row index(offset, not position)"""
        ##Printing the top walls:
        for cell in self.grid[row_number]:
            if cell.north_wall:
                print(f"{Display.print_characters["top_wall"]}" * Display.print_total_width, end ="")
            else:
                print(f"{Display.print_characters["Cell"]}" * Display.print_total_width, end ="")

        print("\n",end="")

        ##Printing the cells:
        for height in  range(Display.print_cell_height):
            for cell in self.grid[row_number]:
                if cell.west_wall:
                    print(f"{Display.print_characters["side_wall"]}" * Display.print_wall_width, end="")
                else:
                    print(f"{Display.print_characters["Cell"]}" * Display.print_wall_width, end="")
                print(f"{Display.print_characters["Cell"]}" * Display.print_cell_width, end="")
                if cell.east_wall:
                    print(f"{Display.print_characters["side_wall"]}" * Display.print_wall_width, end="")
                else:
                    print(f"{Display.print_characters["Cell"]}" * Display.print_wall_width, end="")
            height+=1
            print("\n",end="")

        ##Printing the bottom walls:
        for cell in self.grid[row_number]:
            if cell.south_wall:
                print(f"{Display.print_characters["top_wall"]}" * Display.print_total_width, end ="")
            else:
                print(f"{Display.print_characters["Cell"]}" * Display.print_total_width, end ="")


    def print_maze(self):
        """Prints the cells with all the wall data represented in the maze."""
        for row in range(self.maze.height):
            self.print_row(row)
            print("\n",end = "")






    ##All the turtle graphics methods:
    def execute_screen(self):
        """To be called at the end of the program"""
        self.screen.exitonclick()

    def set_parameters(self):
        """Defines the size of the cell based on screen size and number of cells."""
        cell_side = int(((self.screen.window_height()) - (2 * Display.border_offset)) / self.height) ## Calculates on the basis of vertical border
        self.turtle_cell_height = cell_side
        self.turtle_cell_width = cell_side

    def draw_line(self,distance,heading):
        """Draws a line in a certain heading"""
        self.turtle.pendown()
        self.turtle.setheading(heading)
        self.turtle.forward(distance)
        self.turtle.penup()

    def move(self,distance,heading):
        """Moves the turtle in a certain heading without drawing a line."""
        self.turtle.penup()
        self.turtle.setheading(heading)
        self.turtle.forward(distance)

    def home_turtle(self,axis = "xy"):
        """Homes the turtle with the top left corner as reference post border offset."""
        if axis == "x":
            self.turtle.teleport(self.home_x,self.turtle.ycor())
        elif axis == "y":
            self.turtle.teleport(self.turtle.xcor(),self.home_y)
        else:
            self.turtle.teleport(self.home_x,self.home_y)

    def draw_columns(self):
        """Constructs all the vertical column lines for the maze"""
        #Home the turtle
        self.home_turtle()
        #Print the west_walls for all cells
        for column in range(self.height):
            print(column)
            for row in self.grid:
                if row[column].west_wall:
                    self.draw_line(self.turtle_cell_height,270)
                else:
                    self.move(self.turtle_cell_height,270)
            self.home_turtle("y")
            self.turtle.teleport(self.turtle.xcor()+self.turtle_cell_width,self.turtle.ycor())

        #Account for the east_wall of the final cell.
        for cell_number in range(self.height):
            cell = self.grid[cell_number][self.width-1] ##Accessing the last cell
            if cell.east_wall:
                self.draw_line(self.turtle_cell_height, 270)
            else:
                self.move(self.turtle_cell_height, 270)

        self.home_turtle("xy")

    def draw_rows(self):
        """Constructs all the horizontal row lines for the maze."""
        self.home_turtle()
        for row in self.grid:
            for cell in row:
                if cell.north_wall:
                    self.draw_line(self.turtle_cell_width,0)
                else:
                    self.move(self.turtle_cell_width,0)
            self.home_turtle("x")
            self.turtle.teleport(self.turtle.xcor(), self.turtle.ycor() - self.turtle_cell_height)

            ##Accounting for the bottom most cell:
        for cell in self.grid[self.height-1]:
            if cell.south_wall:
                self.draw_line(self.turtle_cell_width,0)
            else:
                self.move(self.turtle_cell_width,0)
        self.home_turtle("xy")

    def display_maze(self):
        """Draws the maze by calling on draw_rows() and draw_columns()"""
        self.turtle.color("Black")
        self.draw_columns()
        self.draw_rows()

    def clear_screen(self):
        self.screen.clear()





    ##Methods for implementing robot path visualization.
    def reverse_y_coordinates(self,y):
        """Translates the actual maze coordinates to the reverse grid coordinates.."""
        return abs((self.height-1)-y)

    def go_to_cell(self,coordinates):
        """Pass start_coordinates as a dictionary in the form: {"x":x,"y":y}."""
        x = self.home_x + (coordinates["x"]*self.turtle_cell_width) + (self.turtle_cell_width/2)
        y = self.home_y - (self.reverse_y_coordinates(coordinates["y"])*self.turtle_cell_height) - (self.turtle_cell_height/2)
        self.turtle.teleport(x,y)

    def display_robot_path(self,path,start_cell):
        self.turtle.color("Green")
        """Displays the robot path."""
        self.go_to_cell(start_cell.coordinates)
        for direction in path:
            if direction == "North":
                self.draw_line(self.turtle_cell_height,90)
            elif direction == "South":
                self.draw_line(self.turtle_cell_height,270)
            elif direction == "East":
                self.draw_line(self.turtle_cell_width,0)
            elif direction == "West":
                self.draw_line(self.turtle_cell_width,180)
