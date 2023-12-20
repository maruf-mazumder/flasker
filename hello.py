from flask import Flask, render_template


# Create a flask instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
	firstname = "Mr. Maruf"
	stuff = "This is bold text"
	favourite_fruits = ["Apple" , "Mango" , "Pineapple" , 43]
	return render_template('index.html', firstname =  firstname, stuff = stuff, favourite_fruits = favourite_fruits)


# localhost:5000:user/john
# @app.route('/user/<name>')
# def user(name):
# 	return "<h1>Hello {} ,  Please shut up!</h1>".format(name)



# localhost:5000:user/john
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name= name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404



# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500