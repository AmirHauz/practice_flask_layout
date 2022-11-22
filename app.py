
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cats")
def cats():
    return render_template('cats.html')

@app.route("/dogs")
def dog():
     return render_template('dogs.html')

@app.route("/sale1")
def sale1():
     return render_template('sale1.html')

@app.route("/sale2")
def sale2():
     return render_template('sale2.html')

@app.route("/sale3")
def sale3():
     return render_template('sale3.html')

@app.route("/sale4")
def sale4():
     return render_template('sale4.html')

@app.route("/sale5")
def sale5():
     return render_template('sale5.html')

@app.route("/sale6")
def sale6():
     return render_template('sale6.html')

@app.route("/test")
def tst():
     return render_template('tst.html')

if __name__ == "__main__":
    app.run(debug=True)

