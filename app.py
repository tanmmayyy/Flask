from flask import Flask



app=Flask(__name__)



@app.route("/")
def learn():
    return "Learning Flask"



if __name__ == "__main__":
    app.run()



