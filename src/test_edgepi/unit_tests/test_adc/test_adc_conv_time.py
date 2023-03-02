"""Unit tests for adc_conv_time.py module"""

import pytest
from edgepi.adc.adc_conv_time import (
    expected_initial_time_delay,
    expected_continuous_time_delay,
    ADC1_CONT_DELAYS,
    ADC1_INITIAL_DELAYS,
    ADC2_CONT_DELAYS,
    ADC2_INITIAL_DELAYS,
)
from edgepi.adc.adc_constants import (
    FilterMode as FILT,
    ADC1DataRate as DR1,
    ADC2DataRate as DR2,
    ADCNum,
)


@pytest.mark.parametrize(
    "adc_num, data_rate, filter_mode, expected",
    [
        (
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2P5.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            # ADC1 PULSE MODE
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2P5.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2P5.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2P5.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2P5.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_5.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_5.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_5.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_5.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_5.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_10.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_10.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_10.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_10.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_10.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_16P6.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_16P6.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_16P6.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_16P6.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_16P6.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_20.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_20.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_20.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_20.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_20.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_50.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_50.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_50.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_50.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_50.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_60.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_60.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_60.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_60.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_60.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_100.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_100.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_100.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_100.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_100.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_400.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_400.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_400.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_400.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_400.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_1200.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_1200.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_1200.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_1200.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_1200.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2400.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2400.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2400.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2400.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_2400.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_4800.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_4800.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_4800.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_4800.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_4800.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_7200.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_7200.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_7200.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_7200.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_7200.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_14400.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_14400.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_14400.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_14400.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_14400.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_19200.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_19200.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_19200.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_19200.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_19200.value.op_code][FILT.FIR.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            FILT.SINC1.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_38400.value.op_code][FILT.SINC1.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            FILT.SINC2.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_38400.value.op_code][FILT.SINC2.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            FILT.SINC3.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_38400.value.op_code][FILT.SINC3.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            FILT.SINC4.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_38400.value.op_code][FILT.SINC4.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            FILT.FIR.value.op_code,
            ADC1_INITIAL_DELAYS[DR1.SPS_38400.value.op_code][FILT.FIR.value.op_code],
        ),
        # ADC2
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            FILT.SINC1.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            FILT.SINC2.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            FILT.SINC3.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            FILT.SINC4.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            FILT.FIR.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            FILT.SINC1.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            FILT.SINC2.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            FILT.SINC3.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            FILT.SINC4.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            FILT.FIR.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            FILT.SINC1.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            FILT.SINC2.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            FILT.SINC3.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            FILT.SINC4.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            FILT.FIR.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            FILT.SINC1.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_800.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            FILT.SINC2.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_800.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            FILT.SINC3.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_800.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            FILT.SINC4.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_800.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            FILT.FIR.value.op_code,
            ADC2_INITIAL_DELAYS[DR2.SPS_800.value.op_code],
        ),
    ],
)
def test_compute_initial_time_delay(adc_num, data_rate, filter_mode, expected):
    if adc_num == ADCNum.ADC_1:
        assert expected_initial_time_delay(adc_num, data_rate, filter_mode) == expected
    else:
        assert expected_initial_time_delay(adc_num, data_rate, filter_mode) == expected


@pytest.mark.parametrize(
    "adc_num, data_rate, expected",
    [
        # ADC1 CONTINUOUS MODE
        (
            ADCNum.ADC_1,
            DR1.SPS_2P5.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_2P5.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_5.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_5.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_10.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_16P6.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_16P6.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_20.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_20.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_50.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_50.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_60.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_60.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_100.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_400.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_1200.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_1200.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_2400.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_2400.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_4800.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_4800.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_7200.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_7200.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_14400.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_14400.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_19200.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_19200.value.op_code],
        ),
        (
            ADCNum.ADC_1,
            DR1.SPS_38400.value.op_code,
            ADC1_CONT_DELAYS[DR1.SPS_38400.value.op_code],
        ),
        # ADC2
        (
            ADCNum.ADC_2,
            DR2.SPS_10.value.op_code,
            ADC2_CONT_DELAYS[DR2.SPS_10.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_100.value.op_code,
            ADC2_CONT_DELAYS[DR2.SPS_100.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_400.value.op_code,
            ADC2_CONT_DELAYS[DR2.SPS_400.value.op_code],
        ),
        (
            ADCNum.ADC_2,
            DR2.SPS_800.value.op_code,
            ADC2_CONT_DELAYS[DR2.SPS_800.value.op_code],
        ),
    ],
)
def test_compute_continuous_time_delay_adc_1(adc_num, data_rate, expected):
    assert expected_continuous_time_delay(adc_num, data_rate) == expected
