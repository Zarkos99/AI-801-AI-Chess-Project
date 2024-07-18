"""Module providing the Architecture class."""

from dataclasses import dataclass

from actuators import Actuators
from sensors import Sensors

@dataclass
class Architecture:
    """Class representing architecture, which is a computing device with sensors and actuators."""

    actuators: Actuators = Actuators()
    sensors: Sensors = Sensors()
