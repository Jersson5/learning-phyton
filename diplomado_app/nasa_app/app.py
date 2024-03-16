from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

api_url = "https://api.nasa.gov/planetary/apod"
api_key= "8haf9dyjSpTYJ915evaGSa4mOdfuJd8rGx3MtNdp"

app.route('/')

def index():
    params = {
        'api_key': api_key
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        return render_template('index.html', data=data)
    else:
        return f"Erorr {response.status_code}"
    
    if __name__ == '__main__':
        app.run(debug=True)

    