from flask import Flask, render_template, request
import requests
from lib import findLinks

app = Flask('musicmap')

@app.route("/")
def index():
	return render_template("player.html")

@app.route("/playlist/", methods=['POST'])
def playlist():
	subred = request.form['subreddit']
	linksdict = findLinks.findsongs("http://www.reddit.com/r/" + subred)
	print linksdict
	return render_template('playlist.html', links = linksdict)

@app.route("/search/")
def search():
	return render_template("index.html")

@app.route("/player/")
def player():
	return render_template("player.html")

@app.route("/hello/")
def hello():
	return render_template("hello.html")

@app.route("/helper.html")
def helper():
	return render_template("helper.html")

@app.route("/welcome/")
def welcome():
	return render_template("welcome.html")

@app.route("/newalbum/", methods=['POST'])
def newalbum():
	user_str = str(request.form['user'])
	key_str = str(request.form['key'])
	artist_str = str(request.form['artist'])
	album_str = str(request.form['album'])
	long_str = "43.5444"
	lat_str = "65.4323"

	payload = {'albumname':album_str,'artist':artist_str, 'userid':user_str,'lat':lat_str, 'lng':long_str}
	r = requests.post('http://172.26.76.32:5000/songlist/add',data=payload)
	return r.text

#data:{user:R.currentUser.get('vanityName'), artist:album.get('artist'), album:album.get('album'), key:album.key},
              

if __name__ == "__main__":
	app.run(debug=True)