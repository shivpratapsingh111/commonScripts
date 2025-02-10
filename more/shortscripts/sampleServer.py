from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all():
    raw_data = request.get_data(as_text=True)
    headers = dict(request.headers)
    method = request.method
    
    log = f"Received {method} request:\nHeaders: {headers}\nBody: {raw_data}\n"
    print(log)
    
    return log, 200

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
