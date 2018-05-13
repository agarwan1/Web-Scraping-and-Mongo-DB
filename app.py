from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    mars_images = mongo.db.mars_images.find_one()
    return render_template("index.html", mars_images=mars_images)


@app.route("/scrape")
def scrape():
    mars_images = mongo.db.mars_images
    mars_images_data = scrape_mars.scrape()
    print("After calling scrape");
    print(mars_images_data)
    mars_images.update(
        {},
        mars_images_data,
        upsert=True
    )
    print("Done Inserting");
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)