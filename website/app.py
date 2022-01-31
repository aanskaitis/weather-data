from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os, sys
import config

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current_dir))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{config.pwd}@localhost/weather_db'
db = SQLAlchemy(app)

measurement = db.Table('measurement', db.metadata, autoload=True, autoload_with=db.engine)
city = db.Table('city', db.metadata, autoload=True, autoload_with=db.engine)
weather = db.Table('weather', db.metadata, autoload=True, autoload_with=db.engine)


@app.route('/')
def index():
    results = db.session.query(measurement).order_by(db.desc(measurement.columns.id)).limit(51).all()
    return render_template('index.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)