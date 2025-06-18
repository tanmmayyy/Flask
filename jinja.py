from flask import Flask, render_template, request, redirect, url_for



app=Flask(__name__)



@app.route("/")
def learn():
    return "<html><H1>learning flask<H1><html>"



@app.route ("/index")
def index():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/form",methods = ["GET","POST"])
def form ():
    if request.method == "POST":
        name = request.form["name"]
        return f" hello {name}!"
    return render_template("form.html")




@app.route("/submits",methods = ["GET","POST"])
def submits ():
    if request.method == "POST":
        name = request.form["name"]
        return f" hello {name}!"
    return render_template("form.html")


# variable route 

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template("result.html", result = res)



@app.route("/successres/<int:score>")
def successres(score):
    res = "PASSED" if score > 50 else "FAILED"
    exp = {"score": score, "res": res}
    return render_template("result1.html", result=exp)



@app.route("/successif/<int:score>")
def successif(score):
    return render_template ("result.html", results = score)




@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template("result.html", result = score)


@app.route("/submit", methods = ["POST","GET"])
def submit():
    total_score = 0
    if request.method=="POST":
        subject1 = float (request.form["subject1"])
        subject2 = float (request.form["subject2"])
        subject3 = float (request.form["subject3"])
        subject4 = float (request.form["subject4"])
        
        total_score = (subject1 + subject2 + subjnect3 + subject4)/4
        
        
        return redirect(url_for("successres", score = total_score))



if __name__ == "__main__":
    app.run(debug = True)



