import arcade
import random

r, g, b = (random.randint(0, 100) for o in range(3))

x = (random.randint(1, 2000))
y = (random.randint(200, 800))

color_list = [(201, 255, 229), (178, 132, 190), (93, 138, 168), (175, 0, 42), (240, 248, 255), (227, 38, 54), (196, 98, 16), (229, 43, 80), (171, 39, 79), (59, 122, 87), (255, 191, 0), (255, 126, 0), (255, 3, 62), (153, 102, 204), (164, 198, 57), (0, 255, 255), (127, 255, 212), (165, 42, 42), (86, 130, 3), (255, 145, 175)]
print(random.choices(color_list, weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k = 20))

class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       print('boo woomp')


   def on_draw(self):
    """
    C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
    de votre jeu à l'écran.
    """

    arcade.start_render()

    arcade.draw_circle_filled(x, y, 200, (r, g, b))
    arcade.draw_circle_filled(x, y, 200, (r, g, b))


def main():

   window = MyGame(2000, 1080, "Drawing Example")

   arcade.run()


main()
