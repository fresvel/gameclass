import sys

from game.game_object import GameObject
def main():
    print("Starting the game...!")
    go = GameObject(400, 200)
    print(go)
    go.render()

if __name__=='__main__':
    print("Init as main")
    sys.exit(main())