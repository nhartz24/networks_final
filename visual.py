from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='C:\Users\noaha\networks')

# Sample node data
nodes = [
    {"id": 1, "ip": "192.168.0.1", "connected_nodes": [2, 3]},
    {"id": 2, "ip": "192.168.0.2", "connected_nodes": [1, 3]},
    {"id": 3, "ip": "192.168.0.3", "connected_nodes": [1, 2]},
]

@app.route('/')
def open_html_file():
    return render_template('visual.html')

if __name__ == '__main__':
    app.run(debug=True)
    
