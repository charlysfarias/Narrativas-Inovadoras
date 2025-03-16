from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def criar_grafico():
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]
    plt.plot(x, y, marker='o')
    plt.title("Exemplo de Gráfico")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route("/")
def home():
    grafico = criar_grafico()
    return f'<img src="data:image/png;base64,{grafico}" />'

if __name__ == "__main__":
    app.run(debug=True)