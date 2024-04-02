from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("shows.csv")
x = data.drop(columns=["games"])
y = data["games"]
model = DecisionTreeClassifier()
model.fit(x.values ,y)


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
    Strategy = 0
    Sports = 0
    Racing = 0
    Adventure = 0

    if request.method == "POST":
        Sstrategy = request.form[strategy""]
        Ssports = request.form["sports"]
        Ppuzzle = request.form["puzzle"]
        Aadventure = request.form["adventure"]

        strategy = Sstrategy
        sports = Ssports
        puzzle = Ppuzzle
        adventure = Aadventure

    predicted_value = model.predict([[strategy,sports,puzzle,adventure]])

    return render_template("index.html" ,firstname=predicted_value[0])


if __name__ == "__main__":
    app.run(debug=True)
