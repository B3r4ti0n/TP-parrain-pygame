import pygame as pg
import pyscroll
import pytmx as pt
import pyscroll as ps
import pytmx.util_pygame
from player import Player

class Game:

    def __init__(self):
        # Create game's window
        self.heigth = 320
        self.width = 480
        self.screen = pg.display.set_mode((self.width, self.heigth))
        pg.display.set_caption('test')

        # Load map (tmx)
        tmx_data = pt.util_pygame.load_pygame('map_1_0.tmx')
        map_data = ps.TiledMapData(tmx_data)
        map_layer = ps.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #map_layer.zoom = 1

        #generate player
        player_position = tmx_data.get_object_by_name('player')
        self.player = Player(player_position.x, player_position.y)

        # Draw layer's group
        self.group = ps.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pg.key.get_pressed()

        if pressed[pg.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pg.K_LEFT]:
            if self.player.position[0] >= 0:
                self.player.move_left()
                self.player.change_animation('left')

        elif pressed[pg.K_RIGHT]:
            if self.player.position[0] <= 450:
                print(self.player.position[0])
                self.player.move_right()
                self.player.change_animation('right')

    def run(self):

        clock = pg.time.Clock()

        # Loop game's life
        running = True

        while running:

            if self.player.position[1] <= 176:
                self.player.gravity_player()
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            clock.tick(60)

        pg.quit()
