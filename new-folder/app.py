from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.linear_model import LogisticRegression


modelb = joblib.load("brest.pkl")
modelp = joblib.load("pl.pkl")
modell = joblib.load("lung (1).pkl")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/breast.html")
def breast():
    return render_template("breast.html")


@app.route("/lung.html")
def lung():
    return render_template("lung.html")


@app.route("/pro.html")
def pro():
    return render_template("pro.html")


@app.route("/predictb", methods=["POST"])
def predictb():
    if request.method == "POST":
        neitro = request.form["RM"]
        phosph = request.form["TM"]
        potas = request.form["PM"]
        tempa = request.form["AM"]
        humi = request.form["SM"]
        phv = request.form["AS"]
        rainfall = request.form["SS"]
        inputs = [
            float(neitro),
            float(phosph),
            float(potas),
            float(tempa),
            float(humi),
            float(phv),
            float(rainfall),
        ]
        ans = modelb.predict([inputs])
        if ans[0] != "B":
            return render_template("neg.html")
        else:
            return render_template("result.html")
    return render_template("breast.html")


@app.route("/predictl", methods=["POST"])
def predictl():
    if request.method == "POST":
        neitrol = request.form["Ge"]
        phosphl = request.form["Ag"]
        potasl = request.form["smo"]
        tempal = request.form["YF"]
        humil = request.form["AX"]
        phvl = request.form["AC"]
        rainfalll = request.form["cou"]
        lastl = request.form["CP"]
        inputs = [
            float(neitrol),
            float(phosphl),
            float(potasl),
            float(tempal),
            float(humil),
            float(phvl),
            float(rainfalll),
            float(lastl),
        ]
        ans = modell.predict([inputs])
        if ans[0] == "YES":
            return render_template("neg.html")
        else:
            return render_template("result.html")
    return render_template("breast.html")


@app.route("/predictp", methods=["POST"])
def predictp():
    if request.method == "POST":
        neitrop = request.form["RA"]
        phosphp = request.form["TX"]
        potasp = request.form["PM"]
        tempap = request.form["AA"]
        humip = request.form["SN"]
        phvp = request.form["CN"]
        rainfallp = request.form["SM"]
        lastp = request.form["FD"]
        inputs = [
            float(neitrop),
            float(phosphp),
            float(potasp),
            float(tempap),
            float(humip),
            float(phvp),
            float(rainfallp),
            float(lastp),
        ]
        ans = modelp.predict([inputs])
        if ans[0] != "B":
            return render_template("neg.html")
        else:
            return render_template("result.html")
    return render_template("pro.html")


if __name__ == "__main__":
    app.run(
