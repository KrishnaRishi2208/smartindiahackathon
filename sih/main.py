import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
current_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,"final_taskdb3.sqlite3")
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()
class User(db.Model):
	__tablename__='user'
	user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String,nullable=False)
	email = db.Column(db.String, unique=True,nullable=False)
	password =db.Column(db.String,nullable=False)


@app.route("/",methods=["Get","Post"])

def userlogin():
	if request.method=="GET":
		return render_template("mainpage.html")
		
	elif request.method=="POST":
		global usersct
		user_name=request.form["email"]
		password=request.form["password"]
		user1=User.query.filter_by(email=user_name).first()
		userpass=user1.password
		if password==userpass:
			return redirect("/dashboard")  	
	else:
		print("Error , refresh the page")

if __name__=="__main__":
	app.run(
		host='0.0.0.0',
		debug=False,
		port=8080)
