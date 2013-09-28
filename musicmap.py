from flask import Flask, render_template, request

from lib import findLinks

app = Flask('musicdisc')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/playlist/", methods=['POST'])
def playlist():
	subred = request.form['subreddit']
	linksdict = findLinks.findsongs("http://www.reddit.com/r/" + subred)
	print linksdict
	return render_template('playlist.html', links = linksdict)

if __name__ == "__main__":
	app.run(debug=True)