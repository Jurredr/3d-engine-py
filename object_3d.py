import pygame as pg
from matrix_operations import *
from numba import njit


@njit(fastmath=True)
def any(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object3D:
    def __init__(self, render, vertices, faces) -> None:
        self.render = render

        # Vertices and faces (vertex indices)
        self.vertices = np.array([np.array(v) for v in vertices])
        self.faces = np.array([np.array(face) for face in faces])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        # Apply projection
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix

        # Normalize and cut off coordinates outside view
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        # Prepare faces
        for face in self.faces:
            polygon = vertices[face]
            if not any(polygon, self.render.H_WIDTH, self.render.H_HEIGHT):
                pg.draw.polygon(self.render.screen,
                                pg.Color('orange'), polygon, 3)

        for vertex in vertices:
            if not any(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                pg.draw.circle(self.render.screen,
                               pg.Color('white'), vertex, 6)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)
