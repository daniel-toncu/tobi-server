"""
"""

from drivers.i2c.pca9685 import Pca9685I2cDriver


class ServoDriver(Pca9685I2cDriver):
    """
    """

    def __init__(self, channel, frequency=60):
        """
        """

        super(ServoDriver, self).__init__(channel, frequency)
