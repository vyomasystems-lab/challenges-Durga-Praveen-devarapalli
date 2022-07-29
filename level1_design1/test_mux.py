# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.sel.value=0
    dut.inp1.value=2
    print(dut.out.value)
    cocotb.log.info('##### CTB: Develop your test here ########')
