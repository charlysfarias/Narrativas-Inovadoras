from fastapi import FastAPI
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import plotly.express as px
import pandas as pd

app = FastAPI()

def generate_radar_chart():
    labels = ["A", "B", "C", "D", "E"]
    values = [4, 7, 3, 8, 6]
    
    fig = px.line_polar(r=dict(zip(labels, values)), theta=labels, line_close=True)
    return fig.to_json()

def generate_line_chart():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig = px.line(x=x, y=y, labels={"x": "Time", "y": "Value"})
    return fig.to_json()

@app.get("/radar")
async def radar_chart():
    return {"chart": generate_radar_chart()}

@app.get("/line")
async def line_chart():
    return {"chart": generate_line_chart()}
