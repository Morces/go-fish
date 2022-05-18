from flask import Flask,render_template
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
app = Flask(__name__)


@app.route('/')
def index():

    

    bootstrap.init_app(app)



    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)