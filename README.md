# Documentación de la Librería de Juego

Esta documentación describe las clases y funcionalidades principales de la librería para la creación de juegos. La librería se enfoca en objetos del juego, objetos movibles, proyectiles y naves.

## Clases Principales

### `GameObject`

- **Propósito**: Clase base para todos los objetos del juego.
- **Atributos**:
  - `_pos`: Diccionario que contiene la posición `x` e `y` del objeto.
- **Métodos**:
  - `__init__(self, x, y)`: Constructor de la clase. Inicializa la posición del objeto con los valores `x` e `y` dados.
  - `render(self)`: Imprime la representación del objeto (llama a `__str__`).
  - `__str__(self)`: Retorna una cadena que describe la posición del objeto en el formato "GameObject at {x},{y}".

### `MovableObject`

- **Propósito**: Clase base para objetos que pueden moverse en el juego.
- **Hereda de**: `GameObject`.
- **Atributos**:
  - `_speed`: Velocidad de movimiento del objeto.
  - `_move_direction`: Dirección de movimiento (Vertical u Horizontal).
  - `_direction`: Dirección del movimiento actual (Arriba, Abajo, Izquierda, Derecha, Estático).
  - `__flag_direction`: Flag interno para gestionar la dirección de movimiento.
- **Métodos**:
  - `__init__(self, x, y, speed, move_direction)`: Constructor. Inicializa la posición, velocidad y dirección de movimiento.
  - `handle_input(self, direction)`: Maneja la entrada de dirección, actualizando la dirección de movimiento del objeto. Si la dirección dada es consistente con la dirección de movimiento del objeto, actualiza el flag de dirección. En caso contrario, imprime "Movement not allowed!".
  - `update(self, delta_time)`: Actualiza la posición del objeto basándose en la velocidad, la dirección y el tiempo transcurrido.
  - `__str__(self)`: Retorna una cadena que describe la posición del objeto, la dirección de movimiento y la velocidad.

### `Projectile`

- **Propósito**: Representa un proyectil en el juego.
- **Hereda de**: `MovableObject`.
- **Atributos**:
  - `__coalition`: Indica a qué bando pertenece el proyectil.
- **Métodos**:
  - `__init__(self, x, y, speed, coalition)`: Constructor. Inicializa la posición, velocidad y coalición del proyectil. La dirección del proyectil es siempre Vertical.
  - `__str__(self)`: Retorna una cadena que describe al proyectil, incluyendo su coalición y la información de `MovableObject`.

### `Ship`

- **Propósito**: Representa una nave en el juego.
- **Hereda de**: `MovableObject`.
- **Atributos**:
  - `__projectiles`: Lista de proyectiles disparados por la nave.
  - `__coalition`: Indica a qué bando pertenece la nave.
- **Métodos**:
  - `__init__(self, x, y, speed, coalition)`: Constructor. Inicializa la posición, velocidad y coalición de la nave. La dirección de movimiento de la nave es siempre Horizontal.
  - `fire(self)`: Crea un nuevo proyectil en la posición de la nave y lo añade a la lista de proyectiles. El proyectil es creado con una dirección hacia abajo.
  - `update(self, delta_time)`: Actualiza la posición de la nave y de todos sus proyectiles.
  - `__str__(self)`: Retorna una cadena que describe la nave, su coalición y sus proyectiles.

## Enumeraciones

### `MovementDirection`

- **Propósito**: Define las direcciones de movimiento posibles para un `MovableObject`.
  - `Vertical`: Movimiento vertical.
  - `Horizontal`: Movimiento horizontal.

### `Direction`

- **Propósito**: Define las direcciones posibles para la entrada de control de un `MovableObject`.
  - `Static`: Sin movimiento.
  - `Up`: Arriba.
  - `Down`: Abajo.
  - `Left`: Izquierda.
  - `Right`: Derecha.

## Funciones de Prueba

### `testing_movable_object()`

- **Propósito**: Prueba la funcionalidad de la clase `MovableObject`.
- **Acciones**:
  - Crea dos objetos `MovableObject`, uno con movimiento horizontal y otro con movimiento vertical.
  - Prueba el movimiento de ambos objetos en varias direcciones.
  - Imprime mensajes de estado durante las pruebas.

### `main()`

- **Propósito**: Función principal que muestra ejemplos de uso de las clases.
- **Acciones**:
  - Crea instancias de `GameObject`, `MovableObject` y `Ship`.
  - Realiza acciones como mover la nave y disparar proyectiles.
  - Llama a la función `testing_movable_object` para probar la clase `MovableObject`.

## Ejemplo de Uso

El código en la función `main()` muestra cómo crear y usar las diferentes clases. Por ejemplo:

```python
go = GameObject(400, 200)
print(go)  # Imprime: GameObject at 400,200

mo = MovableObject(200, 200, 4, MovementDirection.Vertical)
print(mo)  # Imprime: GameObject at 200,200, Moving Vertical Static at 4

ship = Ship(300, 300, 5, "Friend")
print(ship)  # Imprime: Ship Friend GameObject at 300,300, Moving Horizontal Static at 5

ship.handle_input(Direction.Left)
ship.fire()
ship.update(10)
print(ship)  # Imprime: Ship Friend GameObject at 250,300, Moving Horizontal Left at 5 Fired Projectile Friend GameObject at 300,300, Moving Vertical Down at 10


Para correr el programa ejecute desde la ruta del proyecto `gameplay`

## Salida Esperada

```plaintext
(gameclass) [fresvel@gns3 gameclass]$ code .
(gameclass) [fresvel@gns3 gameclass]$ gameplay 
GameObject at 400,200
GameObject at 200,200, Moving MovementDirection.Vertical Direction.Static at 4
Ship Friend GameObject at 300,300, Moving MovementDirection.Horizontal Direction.Static at 5  
Ship Friend GameObject at 250,300, Moving MovementDirection.Horizontal Direction.Left at 5  Fired Projectile Friend GameObject at 300,400, Moving MovementDirection.Vertical Direction.Down at 10
Movin horizontal object in vertical direction
Movement not allowed!
Movement not allowed!
Movin horizontal object in horizontal direction
Movin vertical object in horizontal direction
Movement not allowed!
Movement not allowed!
Movin vertical object in vertical direction
```