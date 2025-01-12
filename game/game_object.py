class GameObject:
    def __init__(self, x, y):
        self._pos = {"x": x, "y": y}
    
    def render(self):
        print(self)

    def __str__(self):
        return f"GameObject at {self._pos['x']},{self._pos['y']}"
