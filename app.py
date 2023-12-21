from flask import Flask, render_template,request
import requests

app=Flask(__name__)


@app.route("/")
def index():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=44e06e3659d149998fd341c629c5e7ce"
    r=requests.get(url).json()
    cases={
        'articles':r['articles']
    }

    return render_template("index.html", case = cases)

@app.route("/search", methods = ['POST'])
def search():
    q=request.form["search"]
    r=requests.get(f"https://newsapi.org/v2/everything?q={q}&apiKey=44e06e3659d149998fd341c629c5e7ce").json()
    cases={
        'articles':r['articles']
    }

    return render_template("index.html", case = cases)

if __name__ == "__main__":
    app.run(debug=True)