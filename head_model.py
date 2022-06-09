import numpy as np


class Head():

    # 頭のモデル
    head: np.ndarray

    # パラメータ
    theta_x: float
    theta_y: float
    theta_z: float
    scale: float
    slide_x: float
    slide_y: float

    def __init__(self) -> None:
        self.head = HeadModelData.getHeadData()
        self.theta_x = 0
        self.theta_y = 0
        self.theta_z = 0
        self.scale = 1
        self.slide_x = 0
        self.slide_y = 0

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

        self.headself.head @ rx @ ry @ rz

    def scale(self, scale: float) -> None:
        s = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, scale]
        ])
        self.head = self.head @ s

    def slideXY(self, x: float, y: float) -> None:
        s = np.array([
            [x, y, 0],
            [x, y, 0],
            [x, y, 0],
            [x, y, 0],
            [x, y, 0]
        ])
        self.head = self.head + s

    def update(self, theta_x: float, theta_y: float, theta_z: float, scale: float, x: float, y: float) -> None:
        self.theta_x = theta_x
        self.theta_y = theta_y
        self.theta_z = theta_z
        self.scale = scale
        self.slide_x = x
        self.slide_y = y

        self.rotateXYZ(self.theta_x, self.theta_y, self.theta_z)
        self.scale(self.scale)
        self.slideXY(self.slide_x, self.slide_y)

    def getLoss(self, im_head) -> float:
        return np.sum(np.square(self.head - im_head))/len(self.head)


class HeadModelData():
    @staticmethod
    def getHeadData():
        return np.array([
            [
                1339.4813232421875,
                1004.5853271484375,
                0.996397852897644
            ],
            [
                1289.616943359375,
                997.4617919921875,
                0.8979284763336182
            ],
            [
                1360.851806640625,
                954.720947265625,
                0.84747314453125
            ],
            [
                1282.493408203125,
                944.0357666015625,
                0.8657176494598389
            ],
            [
                1303.8638916015625,
                1033.0792236328125,
                0.9093841910362244
            ],
        ])