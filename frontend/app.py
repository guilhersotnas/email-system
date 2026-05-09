from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/send"

@app.route('/', methods=['GET', 'POST'])
def index():

    message = ""

    if request.method == 'POST':

        data = {
            "to": request.form['to'],
            "subject": request.form['subject'],
            "body": request.form['body']
        }

        response = requests.post(BACKEND_URL, json=data)

        message = response.json()['message']

    return render_template(
        'index.html',
        message=message
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
