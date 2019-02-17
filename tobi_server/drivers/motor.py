"""
"""

from drivers.i2c.pca9685 import Pca9685I2cDriver


class MotorDriver(Pca9685I2cDriver):
    """
    """

    def __init__(self):
        """
        """

        super(MotorDriver, self).__init__()
