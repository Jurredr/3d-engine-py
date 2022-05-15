import pygame as py
from matrix_operations import *
from numba import njit


@njit(fastmath=True)
def any(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object3D:
    def __init__(self, render) -> None:
        self.render = render

        # Vertices and faces (vertex indices)
        self.vertices = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (
            1, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
        self.faces = np.array([(0, 1, 2, 3), (4, 5, 6, 7),
                              (0, 4, 5, 1), (2, 3, 7, 6), (1, 2, 6, 5), (0, 3, 7, 4)])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        # Apply projection
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix

        # Normalize and cut off coordinates outside view
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        # Prepare faces
        for face in self.faces:
            polygon = vertices[face]
            if not any(polygon, self.render.H_WIDTH, self.render.H_HEIGHT):
                py.draw.polygon(self.render.screen,
                                py.Color('orange'), polygon, 3)

        for vertex in vertices:
            if not any(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                py.draw.circle(self.render.screen,
                               py.Color('white'), vertex, 6)

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
