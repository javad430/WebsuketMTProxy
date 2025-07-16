from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'MTProto Proxy WebSocket Placeholder'

@app.route('/ws')
def websocket_handler():
    return 'WebSocket proxy endpoint placeholder.'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
