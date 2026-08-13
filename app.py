from flask import Flask, render_template, request
from logic import calculations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        jump_feet = float(request.form.get("feet"))
        jump_inches = float(request.form.get("inches"))
        meters = calculations.convertFtToM(jump_feet, jump_inches)
        print(meters)

        return render_template("index.html", meters=meters)
    
    return render_template("index.html")
    
@app.route("/stats", methods=["GET", "POST"])
def stats():    
    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True)