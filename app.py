from flask import Flask
from flask import render_template
from database import get_all_cats
from database import get_cat

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
	create_cat()
	return render_template("add_cat.html")
	
	pass
if __name__ == '__main__':
   app.run(debug = True)
