
import pygame as pg
from matrix_operations import *


class Camera:
    def __init__(self, render, initial_position):
        # Renderer and position
        self.render = render
        self.position = np.array([*initial_position, 1.0])

        # Orientation vectors
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        # Field of view
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)

        # Clipping planes for view frustum
        self.near_plane = 0.1
        self.far_plane = 100

        # Camera control speeds
        self.moving_speed = 0.3
        self.rotation_speed = 0.015

    def translate_matrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
