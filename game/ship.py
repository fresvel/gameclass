from game.movable_object import MovableObject
from game.movable_object import MovementDirection
from game.movable_object import Direction


class Projectile(MovableObject):
    def __init__(self, x, y, speed, coalition):
        super().__init__(x, y, speed, MovementDirection.Vertical)
        self.__coalition = coalition
    def __str__(self):
        parent_str = super().__str__()  # Llama al método __str__ de la clase base
        return f"Fired Projectile {self.__coalition} {parent_str}"
    
class Ship(MovableObject):

    def __init__(self, x, y, speed, coalition):
        super().__init__(x, y, speed, MovementDirection.Horizontal)
        self.__projectiles = []
        self.__coalition=coalition

    def fire(self):
        projectile = Projectile(self._pos['x'], self._pos['y'], 10, self.__coalition)
        projectile.handle_input(Direction.Down)
        self.__projectiles.append(projectile)
    
    def update(self, delta_time):
        super().update(delta_time)
        for projectile in self.__projectiles:
            projectile.update(delta_time)


    def __str__(self):
        parent_str = super().__str__()
        projectiles_str = ", ".join([str(projectile) for projectile in self.__projectiles])
        return f"Ship {self.__coalition} {parent_str}  {projectiles_str}"
    
