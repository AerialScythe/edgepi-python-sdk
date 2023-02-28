'''integration test for access eeprom'''

# pylint: disable=no-name-in-module
# pylint: disable=wrong-import-position
# https://github.com/protocolbuffers/protobuf/issues/10372
# TODO: I2C Transaction fails without 0.002ms delay

import os
PATH = os.path.dirname(os.path.abspath(__file__))

import time
import logging
import pytest
_logger = logging.getLogger(__name__)

from edgepi.calibration.eeprom_constants import EdgePiMemoryInfo
from edgepi.calibration.edgepi_eeprom import EdgePiEEPROM

@pytest.fixture(name="eeprom")
def fixture_test_dac():
    eeprom = EdgePiEEPROM()
    # eeprom.init_memory()
    return eeprom

@pytest.mark.parametrize("data, address, expected",
                        [(32, 0, 32),
                         (32, 32, 32)
                        ])
def test__byte_write_register(data, address, expected, eeprom):
    initial_data = eeprom.read_memory(address, 1)
    addrx = EdgePiMemoryInfo.USER_SPACE_START_BYTE.value + address
    # pylint: disable=protected-access
    eeprom._EdgePiEEPROM__byte_write_register(addrx, data)
    time.sleep(0.002)
    new_data = eeprom.read_memory(address, 1)
    time.sleep(0.002)
    # pylint: disable=protected-access
    eeprom._EdgePiEEPROM__byte_write_register(addrx, 255)
    _logger.info(f"data to write = {data}")
    _logger.info(f"initial data  = {initial_data}")
    _logger.info(f"new data      = {new_data}")
    assert initial_data[0] != new_data[0]
    assert new_data[0] == expected


@pytest.mark.parametrize("data, address",
                        [
                         (list(range(0,64)),0),
                         (list(range(64,128)),64),
                        ])
def test__page_write_register(data, address, eeprom):
    initial_data = eeprom.read_memory(address, len(data))
    addrx = EdgePiMemoryInfo.USER_SPACE_START_BYTE.value + address
    # pylint: disable=protected-access
    eeprom._EdgePiEEPROM__page_write_register(addrx, data)
    time.sleep(0.002)
    new_data = eeprom.read_memory(address, len(data))
    # pylint: disable=protected-access
    time.sleep(0.002)
    eeprom._EdgePiEEPROM__page_write_register(addrx, [255]*len(data))
    _logger.info(f"data to write = {data}")
    _logger.info(f"initial data  = {initial_data}")
    _logger.info(f"new data      = {new_data}")
    for indx, init_data in enumerate(initial_data):
        assert init_data != new_data[indx]
        assert new_data[indx] == data[indx]