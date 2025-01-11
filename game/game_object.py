class GameObject:
    def __init__(self, x, y):
        self._pos = {"x": x, "y": y}
    
    def render(self):
        print(f"Position in x: {self._pos['x']}, y: {self._pos['y']}")

    def __str__(self):
        return f"GameObject at {self._pos['x']},{self._pos['y']}"
