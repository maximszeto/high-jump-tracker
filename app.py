from flask import Flask, render_template, request
from logic import calculations, database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            jump_feet = float(request.form.get("feet"))
            jump_inches = float(request.form.get("inches"))
            meters = calculations.convertFtToM(jump_feet, jump_inches)
            print(meters)

            return render_template("index.html", meters=meters)

        except ValueError:
            return render_template("index.html")
            
    return render_template("index.html")
    
@app.route("/stats", methods=["GET", "POST"])
def stats():    
    if request.method == "POST":
        newJump = float(request.form.get("jump-height"))
        calculations.addNewLog(newJump, database.highJumpLog) 

    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True)