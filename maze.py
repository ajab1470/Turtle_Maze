"""
Creates a conceptual grid-based maze
The actual maze is a graph of Cells.
Author: Ashley Beckers
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
import random


@dataclass()
class Maze:
    """
    The actual maze
    grid: list of cells
    width: the width of the grid (in number of cells)
    height: the height of the grid (in number of cells)
    """
    grid: List[Cell]
    width: int
    height: int

    def get_cell(self, x, y):
        """
        gets a cell at a specific place in the grid
        :param row: the row of the cell to find
        :param col: the column of the cell to find
        :return: the cell at that row and column
        """
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            return None
        else:
            return self.grid[(y*self.width)+x]


@dataclass()
class Cell:
    """
    A cell in a maze
    neighbors: the cells adjacent to this (None if there is no cell or a wall separates the cells)
    walls: the walls of the Cell. True if the wall is present and False if it is not
    """
    # north_neighbor: Optional[Cell] = None
    # east_neighbor: Optional[Cell] = None
    # south_neighbor: Optional[Cell] = None
    # west_neighbor: Optional[Cell] = None
    north_wall: bool = True
    east_wall: bool = True
    south_wall: bool = True
    west_wall: bool = True

    def __getitem__(self, item):
        """
        gets a wall
        :param item: a tuple of (deltaX, deltaY)
        :return: the specified wall
        """
        if item == (0,-1):
            return self.north_wall
        elif item == (1,0):
            return self.east_wall
        elif item == (0,1):
            return self.south_wall
        elif item == (-1,0):
            return self.west_wall
        else:
            return None

    def __setitem__(self, key, value):
        if key == (0,-1):
            self.north_wall = value
        elif key == (1, 0):
            self.east_wall = value
        elif key == (0, 1):
            self.south_wall = value
        elif key == (-1, 0):
            self.west_wall = value



def make_grid(size):
    """
    creates a maze with no connections between cells.
    connected cells are adjacent cells with no walls in between
    :param size: the dimension of the square grid
    :return: a maze with the specified grid
    """
    grid = []
    maze = Maze(grid, size, size)

    for y in range(size):
        for x in range(size):
            # create a cell and add it to the grid
            cell = Cell()
            grid.append(cell)

    return maze


def add_walls(maze, x, y, walls):
    """
    adds the surrounding walls of a given cell to a list of walls
    :param maze: the maze with the cells
    :param x: the x coordinate of the given cell
    :param y: the y coordinate of the given cell
    :param walls: the list of walls
    post: walls has the surrounding walls of the x,y cell
    """
    start_cell = maze.get_cell(x, y)

    # add all walls of start cell to the wall list
    north_start = maze.get_cell(x, y+1)
    if north_start is not None:
        walls.append(((x,y), (x,y+1)))
    east_start = maze.get_cell(x+1, y)
    if east_start is not None:
        walls.append(((x,y), (x+1,y)))
    south_start = maze.get_cell(x, y-1)
    if south_start is not None:
        walls.append(((x,y), (x,y-1)))
    west_start = maze.get_cell(x-1, y)
    if west_start is not None:
        walls.append(((x,y), (x-1, y)))


def generate_maze(maze):
    """
    creates a maze using a grid of cells using randomized prim's algorithm
    :param maze: the initial maze (with all walls)
    post: cells of grid have walls removed such that a completed maze is formed
    """
    # walls are stored as a tuple in the form (start_cell, end_cell)
    # start cell will always be in the list
    walls = []
    visited_cells = set()
    # get a random cell from the maze
    rand_x = random.randrange(maze.width)
    rand_y = random.randrange(maze.height)
    visited_cells.add((rand_x, rand_y))
    add_walls(maze, rand_x, rand_y, walls)
    # loop until there are no walls left
    while walls:
        wall_ind = random.randrange(len(walls))
        wall = walls[wall_ind]
        walls[wall_ind] = walls[-1]
        walls[-1] = wall
        walls.pop()
        if not wall[1] in visited_cells:
            visited_cells.add(wall[1])
            # get the two cells and calculate their directions to each other
            x1, y1 = wall[0]
            x2, y2 = wall[1]
            start = maze.get_cell(x1, y1)
            unvisited = maze.get_cell(x2, y2)
            start_dir = (x2 - x1, y2 - y1)
            unvisited_dir = (x1 - x2, y1 - y2)
            # remove the wall between them and add unvisited walls to wall list
            start[start_dir] = False
            unvisited[unvisited_dir] = False
            add_walls(maze, x2, y2, walls)

