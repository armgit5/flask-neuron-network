# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, flash, \
                redirect, url_for
    
from logistic_reg import predictImage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, "images/")
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
        
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print(destination)
        upload.save(destination)
        isCat = predictImage(upload.filename)
        if isCat:
            flash("The picture is a cat")
        else:
            flash("The picture is not a cat")
        os.remove(destination)
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=4555, debug=True)