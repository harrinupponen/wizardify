from flask import Flask, url_for, redirect, render_template, request
from app import app

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        return redirect("/result")

    return render_template('index.html')
    

@app.route('/result')
def result():
    return render_template('result.html')