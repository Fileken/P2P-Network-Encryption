from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("main.html")


@app.route('/caesar')
def caesar():
	return render_template("caesar.html")


@app.route('/caesar(custom)')
def caesarcustom():
	return render_template("caesar(custom).html")

@app.route('/a-z')
def az():
	return render_template("a-z.html")

@app.route('/vinzher')
def vinzher():
	return render_template("vinzher.html")

@app.route('/zamena')
def zamena():
	return render_template("zamena.html")


@app.route('/xor')
def xor():
	return render_template("xor.html")



if __name__ == "__main__":
	app.run(debug=True)