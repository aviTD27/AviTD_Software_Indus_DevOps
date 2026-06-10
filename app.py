from FlaskWebProject1 import app

@app.route("/version")
def version():
    return {"version": "2.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
