from game.game_object import GameObject
from enum import Enum

class MovementDirection(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"

class Direction(Enum):
    Static = "Static"
    Up = "Up"
    Down = "Down"
    Left = "Left"
    Right = "Right"

class MovableObject(GameObject):
    def __init__(self, x, y, speed, move_direction):
        super().__init__(x, y)
        self.__speed = speed
        self.__move_direction = move_direction
        self.__direction = Direction.Static 
        self.__flag_direction = 0
            
    def handle_input(self, direction):
        self.__direction = direction
        direction_map = {
            Direction.Up: -1,
            Direction.Down: 1,
            Direction.Left: -1,
            Direction.Right: 1,
            Direction.Static: 0
        }

        if self.__move_direction == MovementDirection.Vertical and self.__direction in [Direction.Up, Direction.Down]:
            self.__flag_direction = direction_map.get(self.__direction, 0)  
        elif self.__move_direction == MovementDirection.Horizontal and self.__direction in [Direction.Left, Direction.Right]:
            self.__flag_direction = direction_map.get(self.__direction, 0) 
        else:
            print("Movement not allowed!")

    def update(self, delta_time):
        axis = "y" if self.__move_direction == MovementDirection.Vertical else "x"
        self._pos[axis] += self.__speed * delta_time * self.__flag_direction
        print(f"Updated position x:{self._pos['x']} y:{self._pos['y']}")

    def __str__(self):
        return f"GameObject at {self._pos['x']},{self._pos['y']}  Moving {self.__move_direction} {self.__direction} at {self.__speed}"

