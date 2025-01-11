import sys

from game.game_object import GameObject
from game.movable_object import Direction
from game.movable_object import MovableObject
from game.movable_object import MovementDirection


def main():
    print("Starting the game...!")
    go = GameObject(400, 200)
    print(go)
    go.render()
    print()
    mo = MovableObject(200,200,4,MovementDirection.Vertical)
    print(mo)

    testing_movable_object()


if __name__=='__main__':
    print("Init as main")
    sys.exit(main())


def testing_movable_object():
    hobj=MovableObject(400,200,4,MovementDirection.Horizontal)
    vobj=MovableObject(400,200,4,MovementDirection.Vertical)

    print("Movin horizontal object in vertical direction")
    hobj.handle_input(Direction.Up)
    hobj.update(1)
    hobj.handle_input(Direction.Down)
    hobj.update(1)
    print("Movin horizontal object in horizontal direction")
    hobj.handle_input(Direction.Left)
    hobj.update(1)
    hobj.handle_input(Direction.Right)
    hobj.update(1)

    print("Movin vertical object in horizontal direction")
    vobj.handle_input(Direction.Left)
    vobj.update(1)
    vobj.handle_input(Direction.Right)
    vobj.update(1)
    print("Movin vertical object in vertical direction")
    vobj.handle_input(Direction.Up)
    vobj.update(1)
    vobj.handle_input(Direction.Down)
    vobj.update(1)