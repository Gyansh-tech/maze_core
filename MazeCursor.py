class MazeCursor:
    """The MazeCursor object is the cursor used to generate the maze:
    Key Methods include:
    ,go_to(x,y)
    ,carve_direction(direction)
    ,go_north()
    ,go_south()
    ,go_east()
    ,go_west()"""

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        self.currentCell = None
        self.stack = []

    def go_to(self,x,y):
        """Sends the cursor to an x and y coordinate"""
        self.x = x
        self.y = y

    def carve_direction(self,direction):
        """Moves the cursor to a specific direction and disables the wall through which it travels"""
        if direction == "North":
            ##Sets the north wall of the current cell to False
            self.currentCell.north_wall = False
            ##Sets the South wall of the cell to the North as False too(So that wall is totally nonexistent)
            self.currentCell.neighbours["North"].south_wall = False
            self.go_north()
        elif direction == "South":
            self.currentCell.south_wall = False
            self.currentCell.neighbours["South"].north_wall = False
            self.go_south()
        elif direction == "East":
            self.currentCell.east_wall = False
            self.currentCell.neighbours["East"].west_wall = False
            self.go_east()
        elif direction == "West":
            self.currentCell.west_wall = False
            self.currentCell.neighbours["West"].east_wall = False
            self.go_west()

    def go_north(self):
        """Sends the cursor one cell up"""
        self.y += 1
    def go_south(self):
        """Sends the cursor one cell down"""
        self.y -= 1
    def go_east(self):
        """Sends the cursor one cell right"""
        self.x += 1
    def go_west(self):
        """Sends the cursor one step left"""
        self.x -= 1



