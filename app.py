from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        return redirect("/result")

    return render_template('index.html')
    

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
