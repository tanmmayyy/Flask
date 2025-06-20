from flask import Flask



app=Flask(__name__)



@app.route("/")
def learn():
    return "Learning Flask from youtube"



@app.route ("/index")
def index():
    return "welcome to index page"



if __name__ == "__main__":
    app.run(debug = True)



