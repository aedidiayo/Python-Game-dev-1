import pgzrun
import random
WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = random.randint(0, 255)
    size = 200  # full side length of the biggest square
    for i in range(25):
        # Rect(left, top, width, height) - centered on the screen
        square = Rect((WIDTH//2 - size//2, HEIGHT//2 - size//2), (size, size))
        screen.draw.rect(square, (r, g, b))
        r = r - 10
        g = g + 10
        size = size - 10  # shrinks by 10 each time (5 per side, like the radius did)

pgzrun.go()
