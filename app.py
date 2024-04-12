from flask import Flask
from flask import render_template

app = Flask(__name__)

def gen_data():


    
    p0 = '[0, 0, 50]'
    p1 = '[0, 1, 100]'
    p2 = '[1, 0, 50]'

    data_str = ', '.join([p0, p1, p2])
    return data_str

@app.route("/")
def hello_world():
    return render_template('index.html',the_name='一个名字')

@app.route("/index.js")
def index_js():
    the_data = gen_data()
    return render_template('index.js', the_data=the_data)

if __name__ == "__main__":
    app.run(debug=True)