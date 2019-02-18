"""
"""

from Adafruit_PCA9685 import PCA9685

from drivers.generics.base import BaseDriver


class Pca9685I2cDriver(BaseDriver):
    """
    """

    MIN_VALUE = 150
    MAX_VALUE = 600

    MID_VALUE = MIN_VALUE + (MAX_VALUE - MIN_VALUE) // 2

    def __init__(self, channel, frequency):
        """
        """

        super(Pca9685I2cDriver, self).__init__()

        self._channel = channel
        self._frequency = frequency

        self._pca9685 = PCA9685()

        self._pca9685.set_pwm_freq(self._frequency)

    def _set_pwm_value(self, value):
        """
        """

        self._pca9685.set_pwm(self._channel, 0, value)

    def set_pwm_value(self, value):
        """
        """

        if value < Pca9685I2cDriver.MIN_VALUE:

            self._set_pwm_value(Pca9685I2cDriver.MIN_VALUE)

            return Pca9685I2cDriver.MIN_VALUE

        if value > Pca9685I2cDriver.MAX_VALUE:

            self._set_pwm_value(Pca9685I2cDriver.MAX_VALUE)

            return Pca9685I2cDriver.MAX_VALUE

        self._set_pwm_value(value)

        return value
