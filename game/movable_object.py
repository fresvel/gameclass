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
        self._speed = speed
        self._move_direction = move_direction
        self._direction = Direction.Static 
        self.__flag_direction = 0
            
    def handle_input(self, direction):
        self._direction = direction
        direction_map = {
            Direction.Up: -1,
            Direction.Down: 1,
            Direction.Left: -1,
            Direction.Right: 1,
            Direction.Static: 0
        }

        if self._move_direction == MovementDirection.Vertical and self._direction in [Direction.Up, Direction.Down]:
            self.__flag_direction = direction_map.get(self._direction, 0)  
        elif self._move_direction == MovementDirection.Horizontal and self._direction in [Direction.Left, Direction.Right]:
            self.__flag_direction = direction_map.get(self._direction, 0) 
        else:
            print("Movement not allowed!")

    def update(self, delta_time):
        axis = "y" if self._move_direction == MovementDirection.Vertical else "x"
        self._pos[axis] += self._speed * delta_time * self.__flag_direction
        
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, Moving {self._move_direction} {self._direction} at {self._speed}"
        #return f"GameObject at {self._pos['x']},{self._pos['y']}  Moving {self._move_direction} {self._direction} at {self._speed}"

