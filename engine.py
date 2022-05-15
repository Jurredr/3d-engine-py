import pygame as pg


class Engine:
    def __init__(self) -> None:
        # Set up PyGame
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

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


if __name__ == '__main__':
    # Initialize and start
    engine = Engine()
    engine.start()
