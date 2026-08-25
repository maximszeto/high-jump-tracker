from flask import Flask, render_template, request, redirect, url_for
from logic import calculations, database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            raw_feet = request.form.get("feet")
            raw_inches = request.form.get("inches")
            if type(raw_feet) == int or float and type(raw_inches) == int or float:
                feet = float(raw_feet)
                inches = float(raw_inches)
                meters = calculations.convertFtToM(feet, inches)
                print(meters)

            return render_template("index.html", meters=meters)

        except ValueError:
            return render_template("index.html")
            
    return render_template("index.html", meters=None)
    
@app.route("/stats", methods=["GET", "POST"])
def stats():    
    if request.method == "POST":
        raw_jump = request.form.get("jump-height", "").strip()
        try:
            new_jump = float(raw_jump)
        except (ValueError, TypeError):
            #flash("Enter a valid numeric jump height.")
            return redirect(url_for("stats"))
            
        ok = calculations.addNewLog(new_jump, database.highJumpLog)
        if ok:
            database.saveData()
            #flash("Jump logged.")
        else:
            pass #flash("Jump must be positive.")
        return redirect(url_for("stats"))
         
    return render_template("stats.html", log=database.highJumpLog)

if __name__ == "__main__":
    app.run(debug=True)