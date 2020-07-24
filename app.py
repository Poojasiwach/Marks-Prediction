from flask import Flask,render_template,redirect,request
from sklearn.externals import joblib

#__name__ == __main__
app = Flask(__name__) #instanitisng the flask object and passing the module name

model = joblib.load("model.pkl")

#creating routes and handling it
@app.route('/') #by default method is get
def hello():
	return render_template("index.html") 
	#flask knows the html files will placed under the templates folder, it is good to place html files in separate folder

@app.route('/',methods=['POST'])
def marks():
	if request.method == 'POST':
		hours = float(request.form['hours'])
		marks = str(model.predict([[hours]])[0][0])

	return render_template("index.html",your_marks = marks)



#to run the server
if __name__ == '__main__':
	#app.debug = True
	app.run(debug=True)