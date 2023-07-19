from flask import Flask, render_template
from config import fdb

app = Flask(__name__)



@app.route('/')
def index():
    # Obtiene los productos de Firebase
    productos = fdb.child("productos").get().val()

    return render_template('index.html', productos=productos)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)