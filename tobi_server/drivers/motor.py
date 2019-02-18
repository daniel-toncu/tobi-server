"""
"""

from drivers.i2c.pca9685 import Pca9685I2cDriver


class MotorDriver(Pca9685I2cDriver):
    """
    """

    def __init__(self, channel, frequency=60, break_value=Pca9685I2cDriver.MID_VALUE):
        """
        """

        super(MotorDriver, self).__init__(channel, frequency)

        self._break_value = break_value

        if (break_value < Pca9685I2cDriver.MIN_VALUE) or (break_value > Pca9685I2cDriver.MAX_VALUE):
            self._break_value = Pca9685I2cDriver.MID_VALUE

    def ebreak(self):
        """
        """

        self._set_pwm_value(self._break_value)
