"""
Creates a conceptual grid-based maze
The actual maze is a graph of Cells.
Author: Ashley Beckers
"""

from dataclasses import dataclass
from typing import Union
import random
import math


@dataclass()
class Location:
    """
    A representation of a point on a grid
    row: the row within the grid of this location
    col: the column within the grid
    id: the unique cell id
    """
    row: int
    col: int
    id: int

    def __hash__(self):
        return self.id


@dataclass()
class Cell:
    """
    A cell in a maze
    row, col: the coordinates of the cell within the board
    neighbors: the four cells surrounding the cell (None if this edge of the cell is against the wall of the maze)
    walls: the walls of the Cell. True if the wall is present and False if it is not
    """
    location: 'Location'
    north_neighbor: Union[None, 'Cell'] = None
    east_neighbor: Union[None, 'Cell'] = None
    south_neighbor: Union[None, 'Cell'] = None
    west_neighbor: Union[None, 'Cell'] = None
    north_wall: bool = True
    east_wall: bool = True
    south_wall: bool = True
    west_wall: bool = True

    def __hash__(self):
        """
        Hashed based on the cell's unique location id
        """
        return self.location.id


def make_grid(size):
    """
    creates a maze grid with no connections between cells.
    A maze grid is represented as a list of cells
    :param size: the dimension of the square grid
    :return: a grid of size by size cells
    """
    grid = []
    for row in range(size):
        for col in range(size):
            # create a cell and add it to the grid
            loc = Location(row, col, (row*size)+col)
            cell = Cell(loc)
            grid.append(cell)

            # connect it to the cells around it
            if col > 0:
                left = grid[(row*size) + col - 1]
                cell.west_neighbor = left
                left.east_neighbor = cell
            if row > 0:
                top = grid[((row-1) * size) + col]
                cell.north_neighbor = top
                top.south_neighbor = cell

    return grid


# Print testers:


def print_cell(cell):
    """
    a tester to confirm a cell looks right
    prints in the form:
    cell location
        North Location ID
        East Location ID
        South Location ID
        West Location ID
    :param cell: the cell
    """
    print("cell ", cell.location, ":", sep="")
    print("\tNorth:", end=" ")

    if cell.north_neighbor is not None:
        print(cell.north_neighbor.location.id)
    else:
        print("None")
    print("\tEast:", end=" ")

    if cell.east_neighbor is not None:
        print(cell.east_neighbor.location.id)
    else:
        print("None")
    print("\tSouth:", end=" ")

    if cell.south_neighbor is not None:
        print(cell.south_neighbor.location.id)
    else:
        print("None")
    print("\tWest:", end=" ")

    if cell.west_neighbor is not None:
        print(cell.west_neighbor.location.id)
    else:
        print("None")


def print_grid(grid):
    """
    a tester to make sure the grid looks right
    :param grid: the maze grid
    """
    size = int(math.sqrt(len(grid)))
    for row in range(size):
        print("row ", row, ":", sep="")
        for col in range(size):
            print_cell(grid[(row*size)+col])
        print()
    print()


if __name__ == '__main__':
    print_grid(make_grid(4))
