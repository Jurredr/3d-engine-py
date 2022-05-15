import math
import pygame as pg
from camera import Camera
from object_3d import Object3D
from projection import Projection


class Engine:
    def __init__(self) -> None:
        # Set up PyGame
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

        # Create objects
        self.create_objects()

    def create_objects(self):
        # Camera and projection
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)

        # Make an object and store it
        self.objects = [Object3D(self)]
        self.objects[0].translate([0.2, 0.4, 0.2])
        self.objects[0].rotate_y(math.pi / 6)

    def start(self) -> None:
        while True:
            # Keep drawing
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            # Display FPS and title
            pg.display.set_caption(
                '3d-engine-py (FPS: ' + str(round(self.clock.get_fps(), 2)) + ')')
            pg.display.flip()
            self.clock.tick(self.FPS)

    def draw(self):
        self.screen.fill(pg.Color('gray69'))
        for object in self.objects:
            object.draw()


if __name__ == '__main__':
    # Initialize and start
    engine = Engine()
    engine.start()
