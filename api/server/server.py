
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')

@app.route('/')
def main():
    
    return render_template('main.html')

@app.route('/documentation')
def documentation():
    
    return render_template('documentation.html')
    

if __name__ == '__main__':
    app.run()