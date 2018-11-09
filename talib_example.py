from __future__ import print_function

import sys
import numpy as np
import matplotlib.pyplot as plt

import talib
from talib.abstract import Function

TEST_LEN = int(sys.argv[1]) if len(sys.argv) > 1 else 100
r = np.arange(TEST_LEN)
idata = np.random.random(TEST_LEN)

def func_example():
    odata = talib.MA(idata)
    upper, middle, lower = talib.BBANDS(idata)
    kama = talib.KAMA(idata)
    plot(odata, upper, middle, lower, kama)

def abstract_example():
    sma = Function('sma')
    input_arrays = sma.get_input_arrays()
    for key in input_arrays.keys():
        input_arrays[key] = idata
    sma.set_input_arrays(input_arrays)
    odata = sma(30) # timePeriod=30, specified as an arg

    bbands = Function('bbands', input_arrays)
    bbands.parameters = {
        'timeperiod': 20,
        'nbdevup': 2,
        'nbdevdn': 2
    }
    upper, middle, lower = bbands() # multiple output values unpacked (these will always have the correct order)

    kama = Function('kama').run(input_arrays) # alternative run() calling method.
    plot(odata, upper, middle, lower, kama)

def plot(odata, upper, middle, lower, kama):
    plt.plot(r, idata, 'b-', label="original")
    plt.plot(r, odata, 'g-', label="MA")
    plt.plot(r, upper, 'r-', label="Upper")
    plt.plot(r, middle, 'r-', label="Middle")
    plt.plot(r, lower, 'r-', label="Lower")
    plt.plot(r, kama, 'g', label="KAMA")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    print('All functions (sorted by group):')
    groups = talib.get_function_groups()
    for group, functions in sorted(groups.items()):
        print('%s functions: %s' % (group, functions))

    if len(sys.argv) == 1 or sys.argv[1] == 'func':
        print('Using talib.func')
        func_example()
    else:
        print('Using talib.abstract')
abstract_example()