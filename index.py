from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/get_music', methods=("POST", "GET"))
def get_music():
    if request.method == "GET":
        return render_template('/get_music.html')
    else:
        pass


if __name__ == 'main':
    app.run('192.168.16.100',9001)

