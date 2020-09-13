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

    def get_cell(self, row, col):
        """
        gets a cell at a specific place in the grid
        :param row: the row of the cell to find
        :param col: the column of the cell to find
        :return: the cell at that row and column
        """
        return self.grid[(row*self.width)+col]


@dataclass()
class Cell:
    """
    A cell in a maze
    neighbors: the cells adjacent to this (None if there is no cell or a wall separates the cells)
    walls: the walls of the Cell. True if the wall is present and False if it is not
    """
    north_neighbor: Optional[Cell] = None
    east_neighbor: Optional[Cell] = None
    south_neighbor: Optional[Cell] = None
    west_neighbor: Optional[Cell] = None
    north_wall: bool = True
    east_wall: bool = True
    south_wall: bool = True
    west_wall: bool = True


def make_grid(size):
    """
    creates a maze with no connections between cells.
    connected cells are adjacent cells with no walls in between
    :param size: the dimension of the square grid
    :return: a maze with the specified grid
    """
    grid = []
    maze = Maze(grid,size,size)

    for row in range(size):
        for col in range(size):
            # create a cell and add it to the grid
            cell = Cell()
            grid.append(cell)

            # connect it to the cells around it
            # if col > 0:
            #     left = grid[(row*size) + col - 1]
            #     cell.west_neighbor = left
            #     left.east_neighbor = cell
            # if row > 0:
            #     top = grid[((row-1) * size) + col]
            #     cell.north_neighbor = top
            #     top.south_neighbor = cell

    return maze



