### fh-matplotlib

Making it easier to show matplotlib charts in FastHTML.

## Usage

You can install this tool by running:

```
python -m pip install fh-matplotlib
```

After this step, it is ready for use! At the moment this package merely contains a decorator. You can use it to wrap any function that generates a matplotlib chart in order for it to return an `Img` for FastHTML to render. In, short you would typically use it like this:

```python
import numpy as np
import matplotlib.pylab as plt
from fh_matplotlib import matplotlib2fasthtml

# This function will return a proper Img that can be rendered
@matplotlib2fasthtml
def matplotlib_function():
    plt.plot(np.arange(25), np.random.exponential(1, size=25))
```

<details>
    <summary><b>Want to see a full example that you could copy and paste directly?</b></summary>

```python
from fh_matplotlib import matplotlib2fasthtml
from fasthtml.common import * 
import numpy as np
import matplotlib.pylab as plt

app, rt = fast_app()  


count = 0
plotdata = []

@matplotlib2fasthtml
def generate_chart():
    global plotdata
    plt.plot(range(len(plotdata)), plotdata)


@app.get("/")
def home():
    return Title("Matplotlib Demo"), Main(
        H1("Matplotlib Demo"),
        P("Nothing too fancy, but still kind of fancy."),
        Div(f"You have pressed the button {count} times.", id="chart"),
        Button("Increment", hx_get="/increment", hx_target="#chart", hx_swap="innerHTML"),
        style="margin: 20px"
    )


@app.get("/increment/")
def increment():
    global plotdata, count
    count += 1
    plotdata.append(np.random.exponential(1))
    return Div(
        generate_chart(),
        P(f"You have pressed the button {count} times."),
    )

serve()
```
</details>

## Roadmap

This repository is originally meant to be simple helper, but if there are more advanced use-cases to consider I will gladly consider them. Please start a conversation by opening up an issue before starting a PR though.
