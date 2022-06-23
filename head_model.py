import numpy as np


class Head():

    # 頭のモデル
    # "L_Eye"
    # "R_Eye"
    # "L_EarBase"
    # "R_EarBase"
    # "Nose"
    head: np.ndarray
    current: np.ndarray

    # パラメータ
    theta_x: float
    theta_y: float
    theta_z: float
    scale: float
    slide_x: float
    slide_y: float

    def getScale(self):
        return self.scale

    def deg_to_rad(self, deg):
        return deg * np.pi / 180

    def __init__(self, nose_x, nose_y) -> None:
        self.head = np.array([
            [2.0085, 2.5248, 1.4081],
            [-2.0085, 2.5248, 1.4081],
            [4.0859, 7.6959, 2.2928],
            [-4.0859, 7.6959, 2.2928],
            [0, 0, 0],
        ])
        self.theta_x = 0
        self.theta_y = 0
        self.theta_z = 0
        self.scale = 1
        # 鼻を原点にする
        self.slide_x = nose_x
        self.slide_y = nose_y

    def _getRotateXMatrix(self, theta_x: float):
        sinx = np.sin(theta_x)
        cosx = np.cos(theta_x)
        return np.array([
            [1, 0, 0],
            [0, cosx, -sinx],
            [0, sinx, cosx]
        ])

    def _getRotateYMatrix(self, theta_y: float):
        siny = np.sin(theta_y)
        cosy = np.cos(theta_y)
        return np.array([
            [cosy, 0, siny],
            [0, 1, 0],
            [-siny, 0, cosy]
        ])

    def _getRotateZMatrix(self, theta_z: float):
        sinz = np.sin(theta_z)
        cosz = np.cos(theta_z)
        return np.array([
            [cosz, -sinz, 0],
            [sinz, cosz, 0],
            [0, 0, 1]
        ])

    def rotateXYZ(self, theta_x: float, theta_y: float, theta_z: float) -> None:
        rx = self._getRotateXMatrix(theta_x)
        ry = self._getRotateYMatrix(theta_y)
        rz = self._getRotateZMatrix(theta_z)

        self.current = self.head @ rx @ ry @ rz

    def scaleXYZ(self, scale: float) -> None:
        s = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, scale]
        ])
        self.current = self.current @ s

    def slideXY(self, x: float, y: float) -> None:
        s = np.array([
            [x, y, 0],
            [x, y, 0],
            [x, y, 0],
            [x, y, 0],
            [x, y, 0]
        ])
        self.current = self.current + s

    def update(self, deg_x: float, deg_y: float, deg_z: float, scale: float) -> None:
        self.theta_x = self.deg_to_rad(deg_x)
        self.theta_y = self.deg_to_rad(deg_y)
        self.theta_z = self.deg_to_rad(deg_z)
        self.scale = scale

        self.rotateXYZ(self.theta_x, self.theta_y, self.theta_z)
        self.scaleXYZ(self.scale)
        self.slideXY(self.slide_x, self.slide_y)

    def get_loss(self, im_head) -> float:
        return np.sum(np.square(self.current[:, :2] - im_head))/len(self.current)
