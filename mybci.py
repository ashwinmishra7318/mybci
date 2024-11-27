from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql 
pymysql.install_as_MySQLdb(
    
)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/login"

db = SQLAlchemy(app)



@app.route("/")                                                                                                                                                                                                                                                                                                                             
def home():
    return render_template('gallery.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/ex")
def ex():
    return render_template('ex.html')

@app.route("/port")
def port():
    return render_template('port.html')




app.run(debug=True)   
