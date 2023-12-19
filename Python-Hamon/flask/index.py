import flask 

app = flask.Flask("hrms")
@app.route("/")
def index():
    return "<p>Hello world</p>"




if __name__ == "__main__":
    app.run()