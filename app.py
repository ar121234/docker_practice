from flask import Flask

app=Flask(__name__)
@app.route("/info")
def lw():
    return "Hello World...\nbye bye!!"

@app.route("/me")
def lwnew():
    return "Aryan Ramteke...\n"
app.run(host="0.0.0.0", port=5000)
