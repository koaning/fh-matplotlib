import numpy as np
import matplotlib.pylab as plt
from fh_matplotlib import matplotlib2fasthtml

# This function will return a proper Img that can be rendered
@matplotlib2fasthtml
def matplotlib_function():
    plt.plot(np.arange(25), np.random.exponential(1, size=25))

def test_no_err():
    matplotlib_function()
