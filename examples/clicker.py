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
        Button("Increment", hx_get="/increment/", hx_target="#chart", hx_swap="innerHTML"),
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