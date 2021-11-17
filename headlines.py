from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

FEED_URL = "http://www.matrix67.com/blog/feed"


@app.route('/')
def get_news():
    feed = feedparser.parse(FEED_URL)
    return render_template("home.html", articles=feed["entries"])


if __name__ == '__main__':
    app.run(port=5000, debug=True)