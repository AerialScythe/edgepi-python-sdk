
"""Digital Output Module"""

import time
from edgepi.gpio.gpio_constants import GpioPins
from edgepi.digital_output.digital_output_constants import DoutPins
from edgepi.gpio.edgepi_gpio import EdgePiGPIO

class InvalidPinName(Exception):
    """Raised invalid pin name"""

class EdgePiDigitalOutput():
    """handling digital output"""

    _dout_aout_pair = {
        DoutPins.DOUT1 : GpioPins.AO_EN1,
        DoutPins.DOUT2 : GpioPins.AO_EN2,
        DoutPins.DOUT3 : GpioPins.AO_EN3,
        DoutPins.DOUT4 : GpioPins.AO_EN4,
        DoutPins.DOUT5 : GpioPins.AO_EN5,
        DoutPins.DOUT6 : GpioPins.AO_EN6,
        DoutPins.DOUT7 : GpioPins.AO_EN7,
        DoutPins.DOUT8 : GpioPins.AO_EN8,
    }
    def __init__(self):
        # To limit access to input functionality, using composition rather than inheritance
        self.gpio = EdgePiGPIO()

    def digital_output_state(self, pin_name: DoutPins = None, state: bool = None):
        """
        change the output state of the pin to the state passed as argument
        Args:
            pin_name (DoutPins): DoutPins enums
            state (bool): True = output high, False, output low
        """
        if state is None:
            raise ValueError(f'Invalid state passed: {state}')
        if pin_name is None or pin_name.value not in [pins.value for pins in DoutPins]:
            raise InvalidPinName(f'Invalid pin name passed: {pin_name}')
        if state:
            self.gpio.set_pin_state(pin_name.value)
        else:
            # In order to safely switch internal MUX circuit, Analog enable pin must be set and
            # cleared with a small time delay. This allows overriding AOUT with DOUT
            self.gpio.set_pin_state(self._dout_aout_pair[pin_name].value)
            self.gpio.clear_pin_state(pin_name.value)
            time.sleep(0.05)
            self.gpio.clear_pin_state(self._dout_aout_pair[pin_name].value)

    def digital_output_direction(self, pin_name: DoutPins = None, direction: bool = None):
        """
        change the output state of the pin to the state passed as argument
        Args:
            pin_name (DoutPins): DoutPins enums
            state (bool): True = direction input, False = direction output
        """
        if direction is None:
            raise ValueError(f'Invalid direction passed: {direction}')
        if pin_name is None or pin_name.value not in [pins.value for pins in DoutPins]:
            raise InvalidPinName(f'Invalid pin name passed: {pin_name}')
        if direction:
            self.gpio.set_pin_direction_in(pin_name.value)
        else:
            self.gpio.set_pin_direction_out(pin_name.value)

    def get_state(self, pin_name: DoutPins = None):
        """
        Get the current state of the specified pin
        Args:
            pin_name (DoutPins): DoutPins enums
        Returns:
            state (Bool): True High, False, Low
            direction (Bool): True Input, False Output
        """
        if pin_name is None or pin_name.value not in [pins.value for pins in DoutPins]:
            raise InvalidPinName(f'Invalid pin name passed: {pin_name}')
        state = self.gpio.read_pin_state(pin_name.value)
        direction = self.gpio.get_pin_direction(pin_name.value)

        return state, direction
