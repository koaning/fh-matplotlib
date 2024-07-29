from fasthtml.common import Img
import matplotlib.pylab as plt
import io
import base64


def matplotlib2fasthtml(func):
    '''
    Ensure that matplotlib yielding function returns a renderable item for FastHTML.

    Usage:

    ```python
    import numpy as np
    import matplotlib.pylab as plt
    from fh_matplotlib import matplotlib2fasthtml

    # This function will return a proper Img that can be rendered
    @matplotlib2fasthtml
    def matplotlib_function():
        plt.plot(np.arange(25), np.random.exponential(1, size=25))
    ```
    '''
    def wrapper(*args, **kwargs):
        # Reset the figure to prevent accumulation. Maybe we need a setting for this?
        plt.figure()

        # Run function as normal
        func(*args, **kwargs)

        # Store it as base64 and put it into an image.
        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()
        return Img(src=f'data:image/jpg;base64, {my_base64_jpgData}')
    return wrapper
