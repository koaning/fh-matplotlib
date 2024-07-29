from fh_matplotlib import matplotlib2fasthtml
from fasthtml.common import * 
import numpy as np
import matplotlib.pylab as plt

app = FastHTML()  


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

from starlette.testclient import TestClient

client = TestClient(app)

def test_clicks():
    for i in range(10):
        client.get('/increment')
    resp = client.get('')
    assert 'You have pressed the button 10 times.' in resp.text
    # To properly test if the chart really shows up I will need to resort to Playwright and I prefer to do that another time
