from flask import Flask,request
from flask import render_template
from database import *



app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def catbook_details(id):
	cat = get_cat(id)
	return render_template("cat.html", cat=cat)

@app.route('/Add_cat', methods=["GET","POST"])
def Add_cat():
	print("Reached Add_Cat")
	if request.method == 'GET':
		return render_template("add_cat.html")
	if request.method == 'POST':
		print("Reached inside GET")
		name = request.form['kitty name']
		print("Error Before")
		create_cat(name)
		return render_template("home.html", cats=get_all_cats())
@app.route('/vote')
def cat_vote():
	vote = cat_vote()
	return render_template("cat.html", vote=)

if __name__ == '__main__':
   app.run(debug = True)
