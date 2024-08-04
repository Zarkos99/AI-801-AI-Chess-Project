"""Module providing the Architecture class."""

from dataclasses import dataclass, field

from actuators import Actuators
from sensors import Sensors

@dataclass
class Architecture:
    """Class representing architecture, which is a computing device with sensors and actuators."""

    sensors: Sensors = field(default_factory=Sensors)
    actuators: Actuators = field(default_factory=Actuators)
