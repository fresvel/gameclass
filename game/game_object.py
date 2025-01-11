class GameObject:
    def __init__(self, x, y):
        self.__pos = {"x": x, "y": y}
    
    def render(self):
        print(f"Position in x: {self.__pos['x']}, y: {self.__pos['y']}")

    def __str__(self):
        return f"GameObject at {self.__pos['x']},{self.__pos['y']}"
