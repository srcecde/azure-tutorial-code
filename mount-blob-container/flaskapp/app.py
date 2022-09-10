import glob
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    images = glob.glob('static/images/*.png')
    return render_template(
        'display.html',
        title="Icons display",
        description="Image loader",
        image_urls=images
    )
