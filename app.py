from flask import app, redirect

app = Flask(__name__)

status = 0

@app.route('/')
def flag():
    if status == 0:
        status = 1
        return "hi"

    else:
        status = 0
        return redirect("http://ssrf.chall.seetf.sg:1337/flag", code=302)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True)
